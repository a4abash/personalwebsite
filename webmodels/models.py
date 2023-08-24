from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Blog(models.Model):
    headline = models.CharField(max_length=200)
    sub_headline = models.CharField(max_length=200,null=True,blank=True)
    image = models.ImageField(null=True,blank=True,upload_to="images",default="images/blog.jpg")
    body = models.TextField(null=True,blank=True)
    created = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag,blank=True,null=True)

    def __str__(self):
        return self.headline
    
class Project(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(null=True,blank=True,upload_to="images",default="images/default.jpg")
    subtitle = models.CharField(max_length=200,default='By Abash')
    body = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.title
    
#supports multiple image in the project
class Projectimage(models.Model):
    image = models.ImageField(upload_to='project/')
    relatedProject = models.ForeignKey(Project,on_delete=models.SET_NULL,blank=True,null=True)

    def __str__(self):
        return self.relatedProject.title