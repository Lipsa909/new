from django.shortcuts import render,redirect
from new.models import *

from django.http import HttpResponse

from django.contrib.auth.models import User




# Create your views here.

def aye(request):
    context={}
    if request.method =="POST":
        d=request.POST
        a=d.get("Name")
        b=d.get("First Name")
        c=d.get("Last Name")
        d=d.get("Age")

        skj.objects.create(Name=a,FirstName=b,LastName=c,Age=d,)

        queryset=skj.objects.all()
        context['new']=queryset
    return render(request,"n1.html",context)

