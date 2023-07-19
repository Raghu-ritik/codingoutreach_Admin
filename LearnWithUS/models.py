from django.db import models

# Create your models here.

class LearnMODEL(models.Model):
    LearnModelid = models.AutoField(primary_key=True)
    LearnTitle = models.CharField(max_length=60,blank=False,unique=True)
    SubLearnHeading = models.CharField(max_length=50,blank=True)
    Videofile = models.FileField(upload_to="LearnWithUS/videos")
    youtubevideolink = models.CharField(max_length=300,null=True,blank=True)
    notedesc = models.TextField(max_length=800)

class notesfile(models.Model):

    Nfileif = models.AutoField(primary_key=True)
    filelink = models.OneToOneField(LearnMODEL,on_delete=models.CASCADE,null=True,blank=True)
    file_title = models.CharField(max_length=100,blank=True)
    file = models.FileField(upload_to="LearnWithUS/videos")