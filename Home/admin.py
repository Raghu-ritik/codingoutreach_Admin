from django.contrib import admin

# Register your models here.
from .models import Contact, Student_B, SocialLinks, Courseenrolled

admin.site.register(Contact)
admin.site.register(Student_B)
admin.site.register(SocialLinks)
admin.site.register(Courseenrolled)

