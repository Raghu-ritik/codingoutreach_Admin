"""C_P_P URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

# from django.conf import settings
# from django.conf.urls.static import static
urlpatterns = [
    path('',views.Home, name='home'),
    path('login',views.login, name="Login"),
    path('register',views.register, name="Register"),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('logout',views.Logout,name="logout"),
    path('contactus',views.contactus,name="ContactUs"),
    path('aboutus',views.aboutus,name="AboutUs"),
    path('usrpage/<str:usrname>',views.Userpage,name="User Page"),
    path('adminpage',views.adminpage,name='admin page'),
    path('adminpage/projectin',views.projin,name='admin page'),
    path('search/', views.search, name="search"),

    # change password
    path('done/', auth_views.PasswordChangeDoneView.as_view(template_name='MailValidation/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='MailValidation/password_change.html', success_url = reverse_lazy("password_change_done")), 
        name='password_change'),

   #Forgot password
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name = "MailValidation/password_reset_form.html", success_url = reverse_lazy("password_reset_complete")), 
    name="password_reset_confirm"),  # 3
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name = "MailValidation/password_reset.html", success_url = reverse_lazy("password_reset_done"), email_template_name = 'MailValidation/forgot_password_email.html'), 
    name="reset_password"),     # 1
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name = "MailValidation/password_reset_sent.html"), 
    name="password_reset_done"),    # 2
    
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name = "MailValidation/password_reset_done.html"), 
    name="password_reset_complete"),   # 4
 

]