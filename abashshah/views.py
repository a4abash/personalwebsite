from django.shortcuts import render,redirect
from webmodels.models import Project,Blog,Tag


# home page for the website
def home(request):
    blog = Blog.objects.filter()[0:3] # sort according to last come firt server lifo order
    project = Project.objects.filter()[0:3]
    bblogs = Blog.objects.all()
    context = {
        'projects':project,
        'probook':blog,
        'bblogs':bblogs,
    }
    return render(request, 'index.html',context)

# particular project section
def project(request,x):
    project = Project.objects.get(id=x)
    context = {
        'project':project
    }
    return render(request,'project.html',context)

# all project section
def allprojects(request):
    project = Project.objects.all()
    context = {
        'allprojects':project
    }
    return render(request,'projects_all.html',context)

# particular blog section
def blog(request,x):
    blog = Blog.objects.get(id=x)
    tags = Tag.objects.get(id=x)
    context = {
        'blog':blog,
        'tags':tags
    }
    return render(request,'blog.html',context)

# all blogs section
def blogs_all(request):
    blogs = Blog.objects.all()
    context = {
        'allblogs':blogs,
    }
    return render(request,'blogs_all.html',context)
