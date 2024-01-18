from django.shortcuts import render,redirect

from toy.models import *


from django.http import HttpResponse

from django.contrib.auth.models import User


# Create your views here.

def ret(request):
    context={}
    if request.method == "POST":
        d=request.POST
        a=d.get("Name")
        b=d.get("Firstname")
        c=d.get("LastName")
        d=d.get("Age")

        tuy.objects.create(Name=a,Firstname=b,Lastname=c,Age=d)

        queryset=tuy.objects.all()
        context['toy']=queryset
    return render(request,"T.html",context)
    
