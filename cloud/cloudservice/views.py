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

    res = requests.post("http://192.168.0.91/identity/v3/auth/tokens",
        headers = {'content-type' : 'application/json'},
        data = json.dumps(payload))

    token = res.headers['X-Subject-Token']

    print(res.headers)

    # index_file = requests.get("http://192.168.56.104/file/index.json", headers=headers)
    
    return JsonResponse({'token': res.headers['X-Subject-Token']}, safe=False)
    #return JsonResponse({'resource' : res.headers }, safe=False)
    # return JsonResponse(res_list, safe=False)
