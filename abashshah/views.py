from django.shortcuts import render,redirect

def home(request):
    return render(request,'index.html')

def project(request):
    return None