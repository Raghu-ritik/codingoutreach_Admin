from django.urls import path,include
from . import views
from django.conf import settings
from django.urls import re_path as url
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('',views.Home2, name='home2'),
    path('LearnView/<int:nkid>/',views.notesview, name='notes View'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_DIR)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
