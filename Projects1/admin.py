from ast import increment_lineno
from pyexpat import model
from django.contrib import admin

# Register your models here.
from .models import Content, Projects1,Pelcon

class ContentInline(admin.TabularInline):
    model = Content

@admin.register(Projects1)
class CustomProjects(admin.ModelAdmin):
    model = Projects1
    list_display = ('projectname','category','rating')
    list_filter = ('category','Availability','rating')

    fieldsets = (
        (None, {'fields': ('projectname','category','desc','creator','datecreated','purpose','Availability','rating')}),
        ('Cover image and video', {'fields': ('Image','introvideo')}),
    )

    inlines = [
        ContentInline
    ]


# admin.site.register(Projects1)
# admin.site.register(Pelcon)
admin.site.register(Content)
