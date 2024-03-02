from unicodedata import category
from django.db import models

# Create your models here.
from os import O_WRONLY, name
from typing import DefaultDict
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class CategoryField(models.Model):
    class Meta:
        verbose_name,verbose_name_plural = "Products Category Field","Products Category Field"
    categoryId = models.AutoField(primary_key=True)
    categoryName = models.CharField(verbose_name="Category Name",max_length=35)
    def __str__(self) -> str:
        return str(self.categoryName)

# Create your models here.
class Products(models.Model):
    class Meta:
        verbose_name,verbose_name_plural = "Site Products","Site Products"
    RATING = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
    )
   

    productid = models.AutoField(primary_key=True)
    productname = models.CharField(verbose_name="Product Name",max_length=100)
    categoryF = models.ForeignKey(CategoryField,verbose_name="Category",on_delete=models.SET_NULL, null=True, blank=True) 
    desc = models.CharField(verbose_name="Description",max_length=500,blank=True)
    creator = models.CharField(verbose_name="Creator Name",max_length=50,blank=True)
    datecreated = models.DateTimeField(verbose_name="Date Created",default=now)
    purpose = models.CharField(verbose_name="Purpose of Product",max_length=250,blank=True)
    Availability = models.BooleanField(verbose_name="Is it Available ?",default=True)
    Image = models.ImageField(verbose_name="Image for Product",upload_to= "Pproducts/images",blank=True)
    rating = models.IntegerField(verbose_name="Rating of Product",choices=RATING,default=4)
    introvideo  = models.FileField(verbose_name="Introduction Video",upload_to="Pproducts/videos",blank=True)
    
    def __str__(self) -> str:
        return str(self.productid)+" "+str(self.productname)

class Content(models.Model):
    class Meta:
        verbose_name,verbose_name_plural = "Product Conent","Product Conent"
    Contentid = models.AutoField(primary_key=True)
    projasso = models.ForeignKey(Products,verbose_name="Project ID",blank=False,on_delete=models.CASCADE,null=True)
    filename = models.CharField(verbose_name="File Name",max_length=50)
    fileup = models.FileField(verbose_name="File Upload",upload_to='Products/filesup/')
    coverup = models.ImageField(verbose_name="Cover Image",upload_to='Products/covers/')

    def __str__(self):
        return self.filename

class ProductsEnrolledUser(models.Model):
    class Meta:
        verbose_name,verbose_name_plural = "Product Enrolled Users","Product Enrolled Users"
    CEid = models.AutoField(primary_key=True)
    profileId = models.ForeignKey(User,verbose_name="User ID",blank=True,on_delete=models.CASCADE,null=True)
    productid = models.ManyToManyField(Products,verbose_name="Courses Enrolled ID",blank=True)

    def __str__(self):
        return  str(self.profileId) + str(self.productid)