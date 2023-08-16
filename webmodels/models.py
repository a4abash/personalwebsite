from django.db import models

# Create your models here.

class Post(models.Model):
    headline = models.CharField(max_length=200)
    sub_headline = models.CharField(max_length=200,null=True,blank=True)
    postimage = models.ImageField(null=True,blank=True,upload_to="images",default="images/blog.jpg")
    body = models.TextField(null=True,blank=True)
    tags = models.ManyToManyField(Tag,null=True)

    def __str__(self):
        return self.headline
    

class Project(models.Model):
    title = models.CharField(max_length=200)
    projectimage = models.ImageField(null=True,blank=True,upload_to="images",default="images/project.jpg")
    subtitle = models.CharField(max_length=200,default='By Abash')
    body = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.title
    
#supports multiple image in the project
class ProImage(models.Model):
    image = models.ImageField(upload_to='kotha/')
    projectImage = models.ForeignKey(Project,on_delete=models.SET_NULL,blank=True,null=True)

    def __str__(self):
        return self.image
