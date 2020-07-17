from django.shortcuts import render,HttpResponse,redirect
from django.conf import settings
from .models import Info
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        usn=request.POST.get('usn')
        year=request.POST.get('year')
        branch=request.POST.get('branch')
        cname=request.POST.get('cname')
        myuserinfo=Info(name=name,email=email,usn=usn,year=year,branch=branch,cname=cname)
        myuserinfo.save()
        messages.info(request,"Your Info Has Been Recorded,Thank You!")
        return redirect('/')
    return render(request,'index.html')