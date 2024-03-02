from django.contrib import admin

# Register your models here.
from .models import(notes1,notesfile)
from .models import CourseFor, categoryOfNotes, subjectOfNotes, branchForNotes, semeserForNotes
# admin.site.register(notesfile)


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
        ('video links', {'fields': ('youtubevideolink','bannerImage')}),
        ('Price', {'fields': ('price',)}),
        ('Notes Description', {'fields': ('notedesc',)}),
    )

    inlines = [
        NotesInline
    ]

    
admin.site.register(CourseFor)
admin.site.register(categoryOfNotes)
admin.site.register(subjectOfNotes)
admin.site.register(branchForNotes)
admin.site.register(semeserForNotes)