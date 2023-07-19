from django.contrib import admin

# Register your models here.
from .models import Products,Content
# admin.site.register(Products)

class ContentInline(admin.TabularInline):
    model = Content

@admin.register(Products)
class CustomProjects(admin.ModelAdmin):
    model = Products
    list_display = ('productname','category','rating')
    list_filter = ('category','Availability','rating')

    fieldsets = (
        (None, {'fields': ('productname','category','desc','creator','datecreated','purpose','Availability','rating')}),
        ('Cover image and video', {'fields': ('Image','introvideo')}),
    )

    inlines = [
        ContentInline
    ]

    

# admin.site.register(Projects1)
# admin.site.register(Pelcon)
admin.site.register(Content)
