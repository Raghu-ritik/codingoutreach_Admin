from pyexpat import model
from statistics import mode
from textwrap import dedent
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from Projects1.models import Projects1

# Create your models here.

class Contact(models.Model):
    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"
    email = models.EmailField()
    name = models.CharField(max_length=50)
    phone_regex = RegexValidator(regex = r'^\+?1?\d{10}$',message = "The format should be exactly be of 10 digits"   )
    contactno = models.CharField(max_length=25,validators=[phone_regex])
    query = models.TextField()

    def __str__(self) -> str:
        return str(self.email) + " <--> " + str(self.contactno)


class Student_B(models.Model):
    class Meta:
        verbose_name = "Users Info"
        verbose_name_plural = "Users Info"
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
    class Meta:
        verbose_name = "Social Links"
        verbose_name_plural = "Social Links"
    SIid = models.AutoField(primary_key=True)
    profileId = models.ForeignKey(User,blank=True,on_delete=models.CASCADE,null=True)
    Github = models.CharField(max_length=200,blank=True,null=True)
    Medium = models.CharField(max_length=200,blank=True,null=True)
    Linkedin = models.CharField(max_length=200,blank=True,null=True)
    filled = models.BooleanField(default=False)

# class AcademicQuali(models.Model):
#     AQid = models.AutoField(primary_key=True)



class ProjectsEnrolled(models.Model):
    class Meta:
        verbose_name = "Project Enrolled Users"
        verbose_name_plural = "Project Enrolled Users"
    CEid = models.AutoField(primary_key=True)
    profileId = models.ForeignKey(User,verbose_name="User ID",blank=True,on_delete=models.CASCADE,null=True)
    courseid = models.ManyToManyField(Projects1,verbose_name="Courses Enrolled ID",blank=True)

class DbLimitException(BaseException):
      pass

class SiteSettings(models.Model):
    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Setings"
    SiteName = models.CharField(default="CodingOutReach",max_length=100)
    SiteHeadSLogan = models.CharField(default="Coding smith's on move",max_length=500)
    SiteUrl = models.CharField(default="www.codingoutrach.com",max_length=200)

    contactusEmail = models.EmailField(default="coonnect@codingoutreach.com")
    adminEmail  = models.EmailField(default="admin@codingoutreach.com")
    
    usersCanRegister = models.BooleanField(default=True,null=True)
    ProjectsAvailable = models.BooleanField(default=False,null=True)
    ProductsAvailable = models.BooleanField(default=False,null=True)
    LearnWithUsAvailable = models.BooleanField(default=False,null=True)
    NotesAvailable = models.BooleanField(default=False,null=True)
    SiteLogo = models.ImageField(upload_to='siteMedia/SiteLogo', default="", null=True, blank=True)
    
    updatedOn = models.DateTimeField(auto_now_add=True,null=True)

    BannerImg1 =  models.ImageField(upload_to='siteMedia\SiteBanner', default="", null=True, blank=True)
    BannerImg2 =  models.ImageField(upload_to='siteMedia\SiteBanner', default="", null=True, blank=True)
    BannerImg3 =  models.ImageField(upload_to='siteMedia\SiteBanner', default="", null=True, blank=True)
    BannerImg4 =  models.ImageField(upload_to='siteMedia\SiteBanner', default="", null=True, blank=True)
    
    NewsApiURL = models.CharField(blank=True,null=True, max_length=200)
    NewAPIToken = models.CharField(blank=True,null=True, max_length=200)

    def __str__(self) -> str:
        return self.SiteName
    