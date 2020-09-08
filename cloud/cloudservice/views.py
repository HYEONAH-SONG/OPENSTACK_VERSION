from django.shortcuts import render 
from django.http import JsonResponse
from .forms import Resource
import json
import requests
import yaml

nowVersion = "V1.0"
heat_template_version = '2015-10-15'

def view(request):
    form = Resource()
    context = {
        'form' : form,
        'version' : nowVersion
    }

    return render(request, 'cloudservice.html', context)

def send(request):

    # 학생수
    student_num = request.POST.getlist('student cnt')[0]
    print(student_num)

    # 운영체제
    send_form=Resource(request.POST)
    i_f = send_form['image']
    image = i_f.data
    print(image)
    
    # 언어
    language = request.POST.getlist('lan')[0]
    print(language)

    # 교육 기간
    edu_term = request.POST.getlist('term')[0]
    print(edu_term)

    # 데이터 유지
    data_maintence = request.POST.getlist('maintenance')[0]
    print(data_maintence)

    #이벤트
    event = request.POST.getlist('event')[0]
    print(event)



    resource = {'Image' : i_f.data }
    
    payload = {
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

    auth_res = requests.post("http://192.168.0.251/identity/v3/auth/tokens",
        headers = {'content-type' : 'application/json'},
        data = json.dumps(payload))

    token = auth_res.headers['X-Subject-Token']

    HOT_res = requests.get("http://192.168.0.251:8080/v1/AUTH_2e2cca5c94e44a859a24b8a63b0ec4cb/files/baseHOT(V1.0).yaml",
        headers={'X-Auth-Token' : token,
                'content-type' : 'application/yaml'}).text

    HOT = yaml.load(HOT_res)


    index_res = requests.get("http://192.168.0.251:8080/v1/AUTH_2e2cca5c94e44a859a24b8a63b0ec4cb/files/index.json",
        headers={'X-Auth-Token' : token,
                'content-type' : 'application/json'}).json()

    major_count = 1
    minor_count = 0
    global nowVersion

    while(True):
        try:
            if index_res["V"+str(major_count)+".0"]["resource"]["language"] == l_f.data and index_res["V"+str(major_count)+".0"]["resource"]["Image"] == i_f.data:
                while(True):
                    try:
                        # find version
                        if index_res["V"+str(major_count)+".0"]["V"+str(major_count)+"."+str(minor_count)] == f_f.data:
                            nowVersion = "V"+str(major_count)+"."+str(minor_count)
                            break
                        else:
                            minor_count += 1
                    except KeyError:
                        # add new minor version
                        index_res["V"+str(major_count)+".0"]["V"+str(major_count)+"."+str(minor_count)] = f_f.data
                        nowVersion = "V"+str(major_count)+"."+str(minor_count)
                        HOT["description"] = "Coding System(" + l_f.data + ")" # language
                        HOT["resources"]["my_instance"]["properties"]["image"] = i_f.data # image
                        HOT["resources"]["my_instance"]["properties"]["flavor"] = f_f.data # flavor
                        break
                break
            major_count += 1
        except KeyError:
            # add new major version
            index_res["V"+str(major_count)+".0"]= { "resource" : resource }
            index_res["V"+str(major_count)+".0"]["V"+str(major_count)+".0"] = f_f.data
            nowVersion = "V"+str(major_count)+"."+str(minor_count)
            HOT["description"] = "Coding System(" + l_f.data + ")" # language
            HOT["resources"]["my_instance"]["properties"]["image"] = i_f.data # image
            HOT["resources"]["my_instance"]["properties"]["flavor"] = f_f.data # flavor
            break

    HOT["heat_template_version"] = heat_template_version

    requests.put("http://192.168.0.251:8080/v1/AUTH_2e2cca5c94e44a859a24b8a63b0ec4cb/files/index.json",
    headers={'X-Auth-Token' : token,
            'content-type' : 'application/json'
            }, data=json.dumps(index_res, indent=4))

    requests.put("http://192.168.0.251:8080/v1/AUTH_2e2cca5c94e44a859a24b8a63b0ec4cb/files/" + nowVersion + ".yaml",
    headers={'X-Auth-Token' : token,
            'content-type' : 'application/yaml'
            }, data=yaml.dump(HOT, sort_keys=False))

    return JsonResponse({
                            'index' : index_res,
                            'token' : token
                        }, safe=False)