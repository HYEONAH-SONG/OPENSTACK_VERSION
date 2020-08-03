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
        {'language' : l_f.data,
        'flavor' : f_f.data,
        'image' : i_f.data,
        }
    ]
    
    data = {
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

    

    res = requests.post("http://192.168.56.104:5000/v3/auth/tokens",
        headers = {'content-type' : 'application/json'},
        data = json.dumps(data))

    #token = identity["X-Subject_Token"]

    return res.headers

    # index_file = requests.get("http://192.168.56.104/file/index.json", headers=headers)

    # return index_file.json
    
    
    #return JsonResponse({'resource' : resource}, safe=False)
    # return JsonResponse(res_list, safe=False)
