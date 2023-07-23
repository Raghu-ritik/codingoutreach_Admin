from xmlrpc.client import TRANSPORT_ERROR
from django.db import models

# Create your models here.

class LearnMODEL(models.Model):
    LearnModelid = models.AutoField(primary_key=True)
    LearnTitle = models.CharField(max_length=60,verbose_name="Title",blank=False,unique=True)
    SubLearnHeading = models.CharField(verbose_name="Sub-Heading ",max_length=50,blank=True)
    Videofile = models.FileField(verbose_name="Video File",upload_to="LearnWithUS/videos",blank=True)
    youtubevideolink = models.CharField(verbose_name="Youtube Video Link",max_length=300,null=True,blank=True)
    notedesc = models.TextField(verbose_name="Notes Description",max_length=800,blank=True)

class notesfile(models.Model):

    Nfileif = models.AutoField(primary_key=True)
    filelink = models.OneToOneField(LearnMODEL,verbose_name="File Link",on_delete=models.CASCADE,null=True,blank=True)
    file_title = models.CharField(max_length=100,verbose_name="File Title",blank=True)
    file = models.FileField(verbose_name="Upload File", upload_to="LearnWithUS/videos")