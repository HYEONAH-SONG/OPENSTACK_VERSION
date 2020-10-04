from django.shortcuts import render 
from django.http import JsonResponse
from .forms import Resource
import json
import requests
import yaml

nowVersion = "V1.0"
heat_template_version = '2015-10-15'
form = Resource()
context = {
        'form' : form,
        'version' : nowVersion
    }

def view(request):
    return render(request, 'cloudservice.html', context) # context로 표현된 cloudservice.html 템플릿의 HttpResponse 객체를 반환.


def send(request):
    
    payload = {   #openstack keystone 토큰을 발급받기 위한 body
        "auth": {
            "identity": {

                "methods": [
                    "password"
                ],
                "password": {
                    "user": {
                        "id": "6443abb0d446410f9f5918d910e767a0 ",
                        "password": "devstack"
                    }
                }
            },
            "scope": {
                "project": {
                    "id": "2e2cca5c94e44a859a24b8a63b0ec4cb"
                }
            }
        }
    }


    #openstack keystone token 발급
    auth_res = requests.post("http://192.168.0.251/identity/v3/auth/tokens",
        headers = {'content-type' : 'application/json'},
        data = json.dumps(payload))

    #발급받은 token
    token = auth_res.headers['X-Subject-Token']

    # openstack container에 있는 baseHOT파일 가져오기
    HOT_res = requests.get("http://192.168.0.251:8080/v1/AUTH_2e2cca5c94e44a859a24b8a63b0ec4cb/files/baseHOT(V1.0).yaml",
        headers={'X-Auth-Token' : token,
                'content-type' : 'application/yaml'}).text

    HOT = yaml.load(HOT_res)

    # container에 있는 index파일 가져오기
    index_res = requests.get("http://192.168.0.251:8080/v1/AUTH_2e2cca5c94e44a859a24b8a63b0ec4cb/files/index.json",
        headers={'X-Auth-Token' : token,
                'content-type' : 'application/json'}).json()

    

    # 웹에서 입력받은 강의실명
    if not request.POST.getlist('class name')[0] :
        return render(request, 'recheckname.html', context)

    stack_name = request.POST.getlist('class name')[0]

    # 웹에서 입력받은 언어
    if not request.POST.getlist('lan') :
        return render(request, 'rechecklan.html', context)
    
    lan = request.POST.getlist('lan')
    lan_cnt = len(lan)
    language = ""
    for i in range(0,lan_cnt):
        if not i == lan_cnt-1 :
            language = language + lan[i] +", "
        else :
            language = language + lan[i]
    


    # 웹에서 입력받은 학생수
    student_num = int(request.POST.getlist('student cnt')[0])
    if student_num < 10 : flavor = "m1.tiny"
    elif student_num > 9 and student_num <20 : flavor = "m1.small"
    elif student_num > 19 and student_num <40 : flavor ="m1.medium"
    elif student_num > 39 and student_num < 80 : flavor = "m1.large"
    elif student_num > 79 and student_num < 160 : flavor = "m1.xlarge"
    #over 160


    # 웹에서 입력받은 운영체제
    send_form=Resource(request.POST)
    i_f = send_form['image']
    image = i_f.data
    if image == "Ubuntu Linux 64-bit" :
        if flavor == "m1.tiny" :
            flavor = "m1.small"
        HOT_image = "bionic-server-cloudimg-amd64" 

    elif image == "CentOS 7 x86-64" :
        if flavor == "m1.tiny" :
            flavor = "m1.small"
        HOT_image = "CentOS-7-x86_64"

    else :
        HOT_image = image
    

    # 웹에서 입력받은 교육 기간
    if request.POST.getlist('latermn') :
        edu_term = request.POST.getlist('term')[0]
    
    # 웹에서 입력받은 데이터 유지 기간
    if request.POST.getlist('maintenance') :
        data_maintence = request.POST.getlist('maintenance')[0]
        
    # 웹에서 입력받은 이벤트 기간
    if request.POST.getlist('event') :
        event = request.POST.getlist('event')[0]
        


    resource = {'language' : language, 'Image' : i_f.data }
    
    
    major_count = 1
    minor_count = 0
    
    global nowVersion 
    
    # HOT 템플릿 버저닝
    while(True):
        try:
            if index_res["V"+str(major_count)+".0"]["resource"]["language"] == language and index_res["V"+str(major_count)+".0"]["resource"]["Image"] == image: # major 버전 기준으로 비교(language, image)
                while(True):  # minor 버전 기준으로 비교
                    try:
                        if index_res["V"+str(major_count)+".0"]["V"+str(major_count)+"."+str(minor_count)] == flavor: # 만약 flavor가 같은게 있으면 (버전 새로 생성 안해도 된다.)
                            nowVersion = "V"+str(major_count)+"."+str(minor_count)
                            break
                        else:
                            minor_count += 1 # 같은 flavor가 없으면 다음 minor 검사하기 위해 카운트.

                    except KeyError:  # 새로운 minor 버전 추가
                        index_res["V"+str(major_count)+".0"]["V"+str(major_count)+"."+str(minor_count)] = flavor
                        nowVersion = "V"+str(major_count)+"."+str(minor_count)
                        HOT["description"] = "Coding System(" + language + ")" # language
                        HOT["resources"]["my_instance"]["properties"]["image"] = HOT_image # image
                        HOT["resources"]["my_instance"]["properties"]["flavor"] = flavor # flavor
                        if image == "Ubuntu Linux 32-bit" or image == "Ubuntu Linux 64-bit" : # image가 Ubuntu Linux 32-bit나 Ubuntu Linux 64-bit일 경우 user_data에 환경 설정을 위한 코드 추가
                            HOT["resources"]["my_instance"]["properties"]["user_data"] = "#cloud-config\nruncmd:\n  - netplan --debug generate\n  - netplan apply\n  - apt-get update -y\n  - apt-get upgrade -y\n"
                            for i in range(0,lan_cnt):
                                if lan[i] == "C": 
                                    HOT["resources"]["my_instance"]["properties"]["user_data"] +="  - sudo apt-get install gcc -y\n" #language가 C언어일 경우 gcc 설치
                                if lan[i] == "C++" :
                                    HOT["resources"]["my_instance"]["properties"]["user_data"] +="  - sudo apt-get install g++ -y\n" #language가 C++언어일 경우 gcc 설치
                        break
                break
            major_count += 1

        except KeyError: # 새로운 major 버전 추가
            index_res["V"+str(major_count)+".0"]= { "resource" : resource }
            index_res["V"+str(major_count)+".0"]["V"+str(major_count)+".0"] = flavor
            nowVersion = "V"+str(major_count)+"."+str(minor_count)
            HOT["description"] = "Coding System(" + language + ")" # language
            HOT["resources"]["my_instance"]["properties"]["image"] = HOT_image # image
            HOT["resources"]["my_instance"]["properties"]["flavor"] = flavor # flavor
            if image == "Ubuntu Linux 32-bit" or image == "Ubuntu Linux 64-bit" :
                HOT["resources"]["my_instance"]["properties"]["user_data"] = "#cloud-config\nruncmd:\n  - netplan --debug generate\n  - netplan apply\n  - apt-get update -y\n  - apt-get upgrade -y\n"
                for i in range(0,lan_cnt):
                    if lan[i] == "C": 
                        HOT["resources"]["my_instance"]["properties"]["user_data"] +="  - sudo apt-get install gcc -y\n"
                    if lan[i] == "C++" :
                        HOT["resources"]["my_instance"]["properties"]["user_data"] +="  - sudo apt-get install g++ -y\n"
            break


    HOT["heat_template_version"] = heat_template_version

    # openstack container에 index파일 저장
    requests.put("http://192.168.0.251:8080/v1/AUTH_2e2cca5c94e44a859a24b8a63b0ec4cb/files/index.json",
    headers={'X-Auth-Token' : token,
            'content-type' : 'application/json'
            }, data=json.dumps(index_res, indent=4))

    # openstack container에 HOT 템플릿 저장
    requests.put("http://192.168.0.251:8080/v1/AUTH_2e2cca5c94e44a859a24b8a63b0ec4cb/files/" + nowVersion + ".yaml",
    headers={'X-Auth-Token' : token,
            'content-type' : 'application/yaml'
            }, data=yaml.dump(HOT, sort_keys=False))

    # openstack container에서 HOT 템플릿 읽어오기
    template = yaml.load(requests.get("http://192.168.0.251:8080/v1/AUTH_2e2cca5c94e44a859a24b8a63b0ec4cb/files/" + nowVersion + ".yaml",
                headers={'X-Auth-Token' : token, 'content-type' : 'application/yaml'}).text)

    # stack 생성을 위한 body
    Hot_body = {
        "stack_name": stack_name,
        "template" : template,
        "timeout_mins": 60
    }

    Json_Hot_body = json.dumps(Hot_body, indent=4)

    # stack 생성
    requests.post("http://192.168.0.251/heat-api/v1/2e2cca5c94e44a859a24b8a63b0ec4cb/stacks",
    headers = {'X-Auth-Token' : token, 'content-type' : 'application/json'}, data = Json_Hot_body)

    # 웹에 index파일 내용과 token 출력
    return JsonResponse({
                            'index' : index_res,
                            'token' : token
                        }, safe=False)

