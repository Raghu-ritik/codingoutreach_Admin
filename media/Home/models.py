from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from Projects1.models import Projects1
# Create your models here.

class Contact(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=50)
    phone_regex = RegexValidator(regex = r'^\+?1?\d{10}$',message = "The format should be exactly be of 10 digits"   )
    contactno = models.CharField(max_length=25,validators=[phone_regex])
    query = models.TextField()


class Student_B(models.Model):
    CATEGORY = (
		('Student', 'Student'),
		('Seller', 'seller'),
        ('Adminuser', 'Adminuser'),
			) 

    studid = models.AutoField(primary_key=True)

    User = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    Susername = models.CharField(max_length=100,null=True,blank=True)
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(unique=True, max_length=200 ,null=False)
    password = models.CharField(max_length=200,null=True,blank=True)
    mobno = models.IntegerField(null=True)
    usertype = models.CharField(max_length=20, null=True, choices=CATEGORY)
    basiverification = models.BooleanField(default=False)
    majorverified = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to='Users/stud_B/',default="profile1.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    colid = models.ImageField(upload_to='Users/stud_B/', default="", null=True, blank=True)

    def __str__(self):
        return self.email

class SocialLinks(models.Model):

    SIid = models.AutoField(primary_key=True)
    profileId = models.ForeignKey(User,blank=True,on_delete=models.CASCADE,null=True)
    Github = models.CharField(max_length=200,blank=True,null=True)
    Medium = models.CharField(max_length=200,blank=True,null=True)
    Linkedin = models.CharField(max_length=200,blank=True,null=True)
    filled = models.BooleanField(default=False)

# class AcademicQuali(models.Model):
#     AQid = models.AutoField(primary_key=True)



class Courseenrolled(models.Model):

    CEid = models.AutoField(primary_key=True)
    profileId = models.ForeignKey(User,blank=True,on_delete=models.CASCADE,null=True)
    courseid = models.ManyToManyField(Projects1,blank=True)