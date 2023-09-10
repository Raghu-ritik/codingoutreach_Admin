from django.contrib import admin

# Register your models here.
from .models import Products, Content, ProductsEnrolledUser, CategoryField
# admin.site.register(Products)

class ContentInline(admin.TabularInline):
    model = Content

@admin.register(Products)
class CustomProjects(admin.ModelAdmin):
    model = Products
    list_display = ('productname','rating')
    list_filter = ('Availability','rating')

    fieldsets = (
        (None, {'fields': ('productname','categoryF','desc','creator','datecreated','purpose','Availability','rating')}),
        ('Cover image and video', {'fields': ('Image','introvideo')}),
    )

    inlines = [
        ContentInline
    ]

    

# admin.site.register(Projects1)
# admin.site.register(Pelcon)
# admin.site.register(Content)
admin.site.register(ProductsEnrolledUser)
admin.site.register(CategoryField)
