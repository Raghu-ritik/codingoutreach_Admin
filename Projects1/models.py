from os import O_WRONLY, name
from typing import DefaultDict
from django.db import models
from django.contrib.auth.models import User
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
    projectname = models.CharField(max_length=100)
    category = models.CharField(max_length=35,null=True,choices=categ)
    desc = models.CharField(max_length=500)
    creator = models.CharField(max_length=50)
    datecreated = models.DateTimeField()
    purpose = models.CharField(max_length=250)
    Availability = models.BooleanField()
    Image = models.ImageField(upload_to= "Projects1/images")
    rating = models.IntegerField(choices=RATING)
    introvideo  = models.FileField(upload_to="Projects1/videos")

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
    filename = models.CharField(max_length=50)
    fileup = models.FileField(upload_to='Projects1/filesup/')
    coverup = models.ImageField(upload_to='Projects1/covers/')

    def __str__(self):
        return self.filename

