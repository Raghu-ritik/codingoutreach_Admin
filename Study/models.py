from django.db import models

# Create your models here.

class notes1(models.Model):
    
    courfor = (
        ('BTech','BTech'),
        ('B.E','B.E'),

    )
    category = (
        ('educational','educational'),
        ('Academic','Academic'),
        ('Misc','Misc')
    )
    subject = (
        ('TOC','TOC'),
        ('DBMS','DBMS'),
        ('Data structure','Data structure'),
        ('ADA','ADA'),
        ('Computer networking','Computer networking'),
        ('compiler Design','compiler Design'),
    )
    branch = (
        ('Computer science','Computer science'),
        ('Mechanical','Mechanical'),
        ('Civil','civil'),
        ('EC','EC'),
        ('EX','EX'),
    )
    sem = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),

    )
    notesid = models.AutoField(primary_key=True)
    notestitle = models.CharField(max_length=60,blank=False)
    category = models.CharField(max_length=50,blank=True,choices=category)
    coursefor = models.CharField(max_length=50,blank=True,choices=courfor)
    subject = models.CharField(max_length=50,blank=True,choices=subject)
    semeter = models.CharField(max_length=30,blank=True)
    branch = models.CharField(max_length=30,blank=True,choices=branch)
    youtubevideolink = models.CharField(max_length=300,null=True,blank=True)
    price = models.IntegerField()
    notedesc = models.TextField(max_length=800)

class notesfile(models.Model):

    Nfileif = models.AutoField(primary_key=True)
    filelink = models.OneToOneField(notes1,on_delete=models.CASCADE,null=True,blank=True)
    file_title = models.CharField(max_length=100,blank=True)
    file = models.FileField(upload_to="Study/notes")