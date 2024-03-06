from django.contrib import admin

# Register your models here.
from .models import Contact, SiteSettings, Student_B, SocialLinks,ProjectsEnrolled

admin.site.register(Contact)
# admin.site.register(Student_B)
admin.site.register(SocialLinks)

admin.site.register(SiteSettings)


@admin.register(Student_B)
class CustomProjects(admin.ModelAdmin):
    model = Student_B
    list_display = ('email','Susername','usertype','basiverification')
    list_filter = ('date_created','majorverified','usertype','basiverification')

    fieldsets = (
 
 
 
    )


