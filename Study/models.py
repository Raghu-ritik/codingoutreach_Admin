from pyexpat import model
from django.db import models

# Create your models here.

class CourseFor(models.Model):
    class Meta:
        verbose_name,verbose_name_plural = "Course","Course"
    CourseId = models.AutoField(primary_key=True)
    CourseName = models.CharField(verbose_name="Course Name",max_length=35)

    def __str__(self) -> str:
        return str(self.CourseName)

class categoryOfNotes(models.Model):
    class Meta:
        verbose_name,verbose_name_plural = "Category","Category"
    CategoryId = models.AutoField(primary_key=True)
    CategoryName = models.CharField(verbose_name="Category Name",max_length=35)
    def __str__(self) -> str:
        return str(self.CategoryName)

class subjectOfNotes(models.Model):
    class Meta:
        verbose_name,verbose_name_plural = "Subject","Subject"
    subjectId = models.AutoField(primary_key=True)
    subjectName = models.CharField(verbose_name="subject Name",max_length=35)
    def __str__(self) -> str:
        return str(self.subjectName)

class branchForNotes(models.Model):
    class Meta:
        verbose_name,verbose_name_plural = "Semester","Semester"
    branchId = models.AutoField(primary_key=True)
    branchName = models.CharField(verbose_name="branch Name",max_length=35)
    def __str__(self) -> str:
        return str(self.branchName)

class semeserForNotes(models.Model):
    class Meta:
        verbose_name,verbose_name_plural = "Branch","Branch"
    semesterId = models.AutoField(primary_key=True)
    semesterName = models.CharField(verbose_name="semester Name",max_length=35)
    def __str__(self) -> str:
        return str(self.semesterName)

class notes1(models.Model):
    class Meta:
        verbose_name,verbose_name_plural = "Notes","Notes"

    notesid = models.AutoField(primary_key=True)
    notestitle = models.CharField(verbose_name="Notes Title",                      max_length=60,            blank=False)
    coursefor = models.ForeignKey(CourseFor,         verbose_name="Course Stream", max_length=50,blank=True, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(categoryOfNotes,    verbose_name="Category",      max_length=50,blank=True, on_delete=models.SET_NULL, null=True)
    subject = models.ForeignKey(subjectOfNotes,      verbose_name="Subject",       max_length=50,blank=True, on_delete=models.SET_NULL, null=True)
    semeter = models.ForeignKey(branchForNotes,      verbose_name="Semester",      max_length=30,blank=True, on_delete=models.SET_NULL, null=True)
    branch = models.ForeignKey(semeserForNotes,      verbose_name="Branch",        max_length=30,blank=True, on_delete=models.SET_NULL, null=True)
    youtubevideolink = models.CharField(             verbose_name="Youtube Video Link",max_length=300,null=True, blank=True)
    price = models.IntegerField(                     verbose_name="Course Price",      blank=True,               default=99)
    notedesc = models.TextField(                     verbose_name="Notes Description", max_length=800,           blank=True)

    def __str__(self) -> str:
        return str(self.notesid)+" "+str(self.notestitle)

class notesfile(models.Model):
    class Meta:
        verbose_name,verbose_name_plural = "Notes File","Notes File"
    Nfileif = models.AutoField(primary_key=True)
    filelink = models.OneToOneField(notes1,          verbose_name="File Link",           on_delete=models.CASCADE,null=True,blank=True)
    file_title = models.CharField(                   verbose_name="File Title",          max_length=100,                    blank=True)
    file = models.FileField(                         verbose_name="Notes File",          upload_to="Study/notes")

    def __str__(self) -> str:
        return str(self.file_title)