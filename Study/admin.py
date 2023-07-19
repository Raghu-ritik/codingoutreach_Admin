from django.contrib import admin

# Register your models here.
from .models import(notes1,notesfile)
# admin.site.register(notes1)
admin.site.register(notesfile)


class NotesInline(admin.TabularInline):
    model = notesfile

@admin.register(notes1)
class CustomProjects(admin.ModelAdmin):
    model = notes1
    list_display = ('notestitle','category','price')
    list_filter = ('category','coursefor','subject','branch','semeter')

    fieldsets = (
        (None, {'fields': ('notestitle','category')}),
        ('Education Category', {'fields': ('coursefor','subject','semeter','branch')}),
        ('video links', {'fields': ('youtubevideolink',)}),
        ('Price', {'fields': ('price',)}),
        ('Notes Description', {'fields': ('notedesc',)}),
    )

    inlines = [
        NotesInline
    ]

    