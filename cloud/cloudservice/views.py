from django.shortcuts import render 
from django.http import JsonResponse
from .forms import Resource
import json
import requests

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

    resource = [
        {
        'language' : l_f.data,
        'flavor' : f_f.data,
        'image' : i_f.data,
        }
    ]
    
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
    
    version_count = 1
    
    while(True):
        try:
            index_res["V"+str(version_count)+".0"]
        except KeyError:
            print("KeyError : " + "V"+str(version_count)+".0")
            new_version = {"V"+str(version_count)+".0" : resource}
            index_dict = json.load(index_res)
            index_dict.update(new_version)
            index_res = json.dumps(index_dict)
            break

    return JsonResponse({
                            'index' : index_res,
                            'token' : token
                        }, safe=False)
