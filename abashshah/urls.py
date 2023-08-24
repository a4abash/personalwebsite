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
    path('blogs_all', views.blogs_all, name='blogs_all'),
    path('signin', views.signin, name='signin'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)