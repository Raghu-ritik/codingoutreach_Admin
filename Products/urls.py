from django.urls import path,include
from . import views
from django.conf import settings

from django.urls import re_path as url
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('',views.ProductIndex, name='product_index'),
    path('input/',views.Input, name='input form for data'),
    path('view/<int:pid>/',views.Productview, name='View the page of project'),
    path('notenrolled',views.NotEnrolled, name='View the page if user is not enrolled into the project'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_DIR)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    