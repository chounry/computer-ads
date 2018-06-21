from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
# from .models import Memory_info
from .models import Mainboard_info

# Create your views here.


def get_all_moth(request): # this the homepage
    all_moths = Mainboard_info.objects.all()
    contexts = {
        'all_moths':all_moths
    }

    return render(request,'motherboard/all_moth.html',context=contexts)

def get_moth_detail(request,slug):
    mainboard_inst = get_object_or_404(Mainboard_info,slug=slug)
    context = {
        "mainboard": mainboard_inst
    }
    return render(request, 'motherboard/moth_detail.html',context=context)
    