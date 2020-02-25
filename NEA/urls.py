from django.contrib import admin #Imports the admin portal path that can be redirected to
from django.contrib.auth import views as login_views #Imports premade django views for login & logout
from django.urls import path, include 
from users import views as profile_views #Imports custom made views for the account registration system
from django.conf import settings #Imports Django settings that can be used for deploying static files
from django.conf.urls.static import static #Imports files necessary for deploying static files

urlpatterns = [                  #urlpatterns links urls to certain views or functions
    path('admin/', admin.site.urls), #Path to admin site
    path('', include('main.urls'), name = "feed"),#Path to main module
    path('register/', profile_views.register, name='register'), #Path to registration view
    path('login/', login_views.LoginView.as_view(template_name='users/login.html'), name = 'login'), #Path to premade django login module
    path('logout/', login_views.LogoutView.as_view(template_name='users/logout.html'), name = 'logout' ), #Path to premade django logout module
    path("connect/<str:operation>/<str:username>/", profile_views.manage_follow, name = 'manage_follow'), #Path to function that manages follows
    path('following/', profile_views.followerList, name = "following"), #Path to following list
    path('profile/', profile_views.profile, name='profile'), #Path to profile view
    path('password-reset/', login_views.PasswordResetView.as_view(template_name = "users/password_reset.html"), name='password_reset'), #Path to change password view
    path('password-reset/done/', login_views.PasswordResetDoneView.as_view(template_name = "users/password_reset_done.html"), name='password_reset_done'), #Path to change password done view
    path('password-reset-confirm/<uidb64>/<token>/', login_views.PasswordResetConfirmView.as_view(template_name = "users/password_reset_confirm.html"), name='password_reset_confirm'), #Path to change password done view
    path('password-reset-complete/', login_views.PasswordResetCompleteView.as_view(template_name = "users/password_reset_complete.html"), name='password_reset_complete'), #Path to change password view
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



