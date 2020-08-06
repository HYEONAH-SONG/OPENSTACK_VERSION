from django.shortcuts import render 
from django.http import JsonResponse
from .forms import Resource
import json
import requests
import yaml

def view(request):
    form = Resource()
    return render(request, 'cloudservice.html', {'form':form})

def send(request):
    send_form=Resource(request.POST)

    l_f = send_form['language']
    f_f = send_form['flavor']
    i_f = send_form['image']

    # class res:
    #     language : l_f.data
    #     flavor : f_f.data
    #     image : i_f.data 

    #  res_list = list(res.objects.values())

    resource = {'language' : l_f.data, 'Image' : i_f.data }
    
    payload = {
        "auth": {
            "identity": {
                "methods": [
                    "password"
                ],
                "password": {
                    "user": {
                        "name": "admin",
                        "domain": {
                            "name": "Default"
                        },
                        "password": "devstack"
                    }
                }
            }
        }
    }

    auth_res = requests.post("http://192.168.0.251/identity/v3/auth/tokens",
        headers = {'content-type' : 'application/json'},
        data = json.dumps(payload))


    token = auth_res.headers['X-Subject-Token']
    
    index_res = requests.get("http://192.168.0.251:8080/v1/AUTH_2e2cca5c94e44a859a24b8a63b0ec4cb/files/index.json",
        headers={'X-Auth-Token' : token,
                'content-type' : 'application/json'}).json()
    
    major_count = 1
    minor_count = 0
    while(True):
        try:
            if index_res["V"+str(major_count)+".0"]["resource"]["language"] == l_f.data and index_res["V"+str(major_count)+".0"]["resource"]["Image"] == i_f.data:
                while(True):
                    try:
                        if index_res["V"+str(major_count)+".0"]["V"+str(major_count)+"."+str(minor_count)] == f_f.data:
                            print("get Version : " + "V"+str(major_count)+"."+str(minor_count))
                            break
                        else:
                            minor_count += 1
                    except KeyError:
                        new_version = {"V"+str(major_count)+"."+str(minor_count) : f_f.data}
                        index_res["V"+str(major_count)+".0"].update(new_version)
                        break
                break
            major_count += 1
        except KeyError:
            new_version = {"V"+str(major_count)+".0" : {"resource" :resource, "V"+str(major_count)+".0" : f_f.data }}
            print(new_version)
            index_res.update(new_version) 
            print(index_res)
            break

    #replace_data = index_res
    """
    requests.put("http://192.168.0.251:8080/v1/AUTH_2e2cca5c94e44a859a24b8a63b0ec4cb/files/index.json",
    headers={'X-Auth-Token' : token,
            'content-type' : 'application/json'
            }, data=replace_data)
    """
    return JsonResponse({
                            'index' : index_res,
                            'token' : token
                        }, safe=False)
