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
    notestitle = models.CharField(verbose_name="Notes Title",max_length=60,blank=False)
    category = models.CharField(verbose_name="Category",max_length=50,blank=True,choices=category)
    coursefor = models.CharField(verbose_name="Course Stream",max_length=50,blank=True,choices=courfor)
    subject = models.CharField(verbose_name="Subject",max_length=50,blank=True,choices=subject)
    semeter = models.CharField(verbose_name="Semester",max_length=30,blank=True)
    branch = models.CharField(verbose_name="Branch",max_length=30,blank=True,choices=branch)
    youtubevideolink = models.CharField(verbose_name="Youtube Video Link",max_length=300,null=True,blank=True)
    price = models.IntegerField(verbose_name="Course Price",blank=True,default=99)
    notedesc = models.TextField(verbose_name="Notes Description",max_length=800,blank=True)

    def __str__(self) -> str:
        return str(self.notesid)+" "+str(self.notestitle)

class notesfile(models.Model):

    Nfileif = models.AutoField(primary_key=True)
    filelink = models.OneToOneField(notes1,verbose_name="File Link",on_delete=models.CASCADE,null=True,blank=True)
    file_title = models.CharField(verbose_name="File Title",max_length=100,blank=True)
    file = models.FileField(verbose_name="Notes File",upload_to="Study/notes")

    def __str__(self) -> str:
        return str(self.file_title)