from django.contrib import admin

from .models import(LearnMODEL,notesfile)
# admin.site.register(LearnMODEL)
# admin.site.register(notesfile)

class NotesFileInline(admin.TabularInline):
    model = notesfile


@admin.register(LearnMODEL)
class CustomLearnModel(admin.ModelAdmin):
    model = LearnMODEL
    list_display = ('LearnTitle','SubLearnHeading')
    list_filter = ('LearnTitle','SubLearnHeading')



    fieldsets = (
        (None, {'fields': ('LearnTitle','SubLearnHeading','youtubevideolink','notedesc')}),
        ('Add Videofile', {'fields': ('Videofile',)}),
    )

    inlines = [
        NotesFileInline
    ]
