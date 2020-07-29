from django.shortcuts import render 
from django.http import JsonResponse
from .forms import Resource

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

   
    return JsonResponse({'resource' : resource}, safe=False)
    # return JsonResponse(res_list, safe=False)
