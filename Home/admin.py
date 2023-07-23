from django.contrib import admin

# Register your models here.
from .models import Contact, Student_B, SocialLinks, Courseenrolled

admin.site.register(Contact)
# admin.site.register(Student_B)
admin.site.register(SocialLinks)
admin.site.register(Courseenrolled)


@admin.register(Student_B)
class CustomProjects(admin.ModelAdmin):
    model = Student_B
    list_display = ('email','Susername','usertype','basiverification')
    list_filter = ('date_created','majorverified','usertype','basiverification')

    fieldsets = (
        (None, {'fields': ('notestitle','category')}),
        ('Education Category', {'fields': ('coursefor','subject','semeter','branch')}),
        ('video links', {'fields': ('youtubevideolink',)}),
        ('Price', {'fields': ('price',)}),
        ('Notes Description', {'fields': ('notedesc',)}),
    )


