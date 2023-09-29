from django.shortcuts import render,redirect
from webmodels.models import Project,Blog,Tag, Projectimage
from django.contrib import messages
from webmodels.forms import BlogForm,ProjectForm,ProjectImgForm
from django.contrib.auth import authenticate, login,logout

# home page for the website
def home(request):
    blog = Blog.objects.filter()[0:3] # sort according to last come firt server lifo order
    project = Project.objects.filter()[0:3]
    # allblogs = Blog.objects.all()
    context = {
        'projects':project,
        'probook':blog,
        # 'bblogs':allblogs,
        'BlogCreationForm': BlogForm(),
        'ProjectCreationForm':ProjectForm(),
        'ProjectImageForm':ProjectImgForm(),
    }
    return render(request, 'index.html',context)

# particular project section
def project(request,x):
    project = Project.objects.get(id=x)
    prjimage = Projectimage.objects.filter(relatedProject_id=project.id)
    context = {
        'project':project,
        'prjimage':prjimage,
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
    # tags = Tag.objects.get(id=x)
    context = {
        'blog':blog,
    #     'tags':tags
    }
    return render(request,'blog.html',context)

# all blogs section
def blogs_all(request):
    blogs = Blog.objects.all()
    context = {
        'allblogs':blogs,
    }
    return render(request,'blogs_all.html',context)

# login page
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html')
    else:
        u = request.POST.get('username')
        p = request.POST['password']
        print(u,p)
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Your Password does not match")
            return redirect('signin')

# Blog adding section
def addBlog(request):
    if request.method == 'GET':
        return ('home')
    else:
        form = BlogForm(request.POST, request.FILES or None)
        print(form)
        if form.is_valid():
            data = form.save(commit=False)
            print(data)
            data.user_id = request.user.id
            data.save()
            return redirect('home')
        else:
            print('not stored')
            return render(request, 'home.html', {'postCreationForm': form})

# Blog delete section
def blog_delete(request,x):
    p = Blog.objects.get(id=x)
    p.delete()
    return redirect('blogs_all')

#Blog edit section
def blog_edit(request,x):
    blog = Blog.objects.get(id=x)
    form = BlogForm(request.POST or None, instance=blog)
    if form.is_valid():
        form.save()
        return redirect('blogs_all')
    context = {
        'form':form,
    }
    return render (request,'blog_edit.html',context)

# Project adding section
def addProject(request):
    if request.method == "GET":
        return ('home')
    else:
        form = ProjectForm(request.POST, request.FILES or None)
        images = request.FILES.getlist('images')
        if form.is_valid:
            data = form.save(commit=False)
            data.user_id = request.user.id
            data.save()
            for img in images:
                photo = Projectimage.objects.create(
                    image=img,
                    relatedProject_id=data.id
                )
            return redirect('home')
        else:
            print('not stored')
            return render(request, 'home.html', {'projectCreationForm': form}) 

# Project edit section
def project_edit(request,x):
    project = Project.objects.get(id=x)
    form = ProjectForm(request.POST, request.FILES or None, instance=project)
    if form.is_valid():
        form.save()
        return redirect('allprojects')
    context = {
        'form': form,
    }
    return render(request, 'project_edit.html',context)

#Project delete section
def project_delete(request,x):
    p = Project.objects.get(id=x)
    p.delete()
    return redirect('allprojects')

# for signout
def signout(request):
    logout(request)
    return redirect('home')