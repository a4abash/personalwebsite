from django.shortcuts import render,redirect
from webmodels.models import Project,Post

# home page for the website
def home(request):
    posts = Post.objects.filter() # sort according to last come firt server lifo order
    project = Project.objects.filter()[0:3]
    context = {
        'posts': posts,
        'projects':project,
    }
    return render(request, 'index.html',context)

def project(request,x):
    project = Project.objects.get(id=x)
    context = {
        'project':project
    }
    return render(request,'project.html',context)
