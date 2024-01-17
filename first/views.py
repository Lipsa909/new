from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.

def lis(request):
        context={}
        if request.method == "POST" :
            d=request.POST
            a=d.get("NAME")
            b=d.get("phNo")
            c=d.get("Address")
        
            tub.objects.create(NAME=a,phNo=b,Address=c,)


            queryset=tub.objects.all()
            context['lipsa']=queryset
           
        return render(request,"l.html",context)