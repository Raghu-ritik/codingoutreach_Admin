from os import O_WRONLY, name
from typing import DefaultDict
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
class Projects1(models.Model):
    RATING = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
    )
    categ = (
        ('Web development','Web development'),
        ('Machine Learning','Machine Learning'),
        ('Data Science','Data Science'),
        ('PHP','PHP'),
        ('C/C++','C/C++'),
        ('Others','Others')
    )    

    projectid = models.AutoField(primary_key=True)
    projectname = models.CharField(verbose_name="Project Name",max_length=100,blank=False)
    category = models.CharField(verbose_name="Category",max_length=35,null=True,choices=categ,blank=True)
    desc = models.CharField(verbose_name="Description",max_length=500,blank=True)
    creator = models.CharField(verbose_name="Creator",max_length=50,blank=True)
    datecreated = models.DateTimeField(verbose_name="Date Created",default=now)
    purpose = models.CharField(verbose_name="Purpose of Project",max_length=250,blank=True)
    Availability = models.BooleanField(verbose_name="Availability of Project",blank=True)
    Image = models.ImageField(verbose_name="Image for Project",upload_to= "Projects1/images",blank=True)
    rating = models.IntegerField(verbose_name="Rating",choices=RATING,default=4)
    introvideo  = models.FileField(verbose_name="Video for Project",upload_to="Projects1/videos",blank=True)

    def __str__(self) -> str:
        return str(self.projectid) + str(self.projectname)

class Pelcon(models.Model):
    name= models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='store/pdfs/')
    cover = models.ImageField(upload_to='store/covers/')

    def __str__(self):
        return self.name


class Content(models.Model):
    Contentid = models.AutoField(primary_key=True)
    projasso = models.ForeignKey(Projects1,blank=False,on_delete=models.CASCADE,null=True)
    filename = models.CharField(verbose_name="File Name",max_length=50)
    fileup = models.FileField(verbose_name="File Upload",upload_to='Projects1/filesup/')
    coverup = models.ImageField(verbose_name="Cover page for File",upload_to='Projects1/covers/')

    def __str__(self):
        return self.filename

