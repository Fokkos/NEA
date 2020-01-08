from django.contrib import admin #Imports the admin portal path that can be redirected to
from django.contrib.auth import views as login_views #Imports premade django views for login & logout
from django.urls import path, include 
from users import views as registration_views #Imports custom made views for the account registration system

urlpatterns = [                  #urlpatterns links urls to certain views or functions
    path('admin/', admin.site.urls), #Path to admin site
    path('', include('main.urls')), #Path to main module
    path('register/', registration_views.register, name='register'), #Path to registration module
    path('login/', login_views.LoginView.as_view(template_name='users/login.html'), name = 'login'), #Path to premade django login module
    path('logout/', login_views.LogoutView.as_view(template_name='users/logout.html'), name = 'logout' ), #Path to premade django logout module
]

