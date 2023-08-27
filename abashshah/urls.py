"""abashshah URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('project/<int:x>', views.project, name='project'), #particular project
    path('allprojects', views.allprojects, name='allprojects'), #list of all projects
    path('blog/<int:x>',views.blog, name ='blog'), #particular blog section
    path('blogs_all', views.blogs_all, name='blogs_all'), #list of all Blogs
    path('signin', views.signin, name='signin'), # login section
    path('addBlog', views.addBlog, name='addBlog'), #Blog post adding section
    path('blog_edit/<int:x>', views.blog_edit, name='blog_edit'), #blog edit section
    path('blog_delete/<int:x>',views.blog_delete,name='blog_delete'), # blog delete section
    path('addProject', views.addProject, name='addProject'), #Project adding section
    path('project_edit/<int:x>', views.project_edit, name='project_edit'), # project edit section
    path('project_delete/<int:x>',views.project_delete,name='project_delete'), # Project delete section

    path('signout', views.signout, name='signout'),  # url for logout function
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)