from django import forms
from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from .models import Project, Blog,Projectimage

class BlogForm(ModelForm):
    headline = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    sub_headline = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    image = forms.ImageField
    tags = forms.CheckboxSelectMultiple
    
    class Meta:
        model = Blog
        fields = '__all__'

class ProjectForm(ModelForm):
    mainimage = forms.ImageField()
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    subtitle = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Project
        fields = '__all__'


class ProjectImgForm(forms.ModelForm):
    image = forms.ImageField(help_text='Add Multiple images')

    class Meta:
        model = Projectimage
        exclude = ['relatedProject']