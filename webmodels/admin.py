from django.contrib import admin
from .models import Project, Post, Projectimage, Tag


# Register your models here.
admin.site.register(Project)
admin.site.register(Post)
admin.site.register(Projectimage)
admin.site.register(Tag)
