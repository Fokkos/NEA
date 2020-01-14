from django.contrib import admin #Imports the admin portal path that can be redirected to
from django.contrib.auth import views as login_views #Imports premade django views for login & logout
from django.urls import path, include 
from users import views as profile_views #Imports custom made views for the account registration system
from django.conf import settings #Imports Django settings that can be used for deploying static files
from django.conf.urls.static import static #Imports files necessary for deploying static files

urlpatterns = [                  #urlpatterns links urls to certain views or functions
    path('admin/', admin.site.urls), #Path to admin site
    path('', include('main.urls'), name = "index"),#Path to main module, specifically the index
    path('', include('main.urls'), name = "search"), #Path to main module, specifically the search function
    path('register/', profile_views.register, name='register'), #Path to registration view
    path('login/', login_views.LoginView.as_view(template_name='users/login.html'), name = 'login'), #Path to premade django login module
    path('logout/', login_views.LogoutView.as_view(template_name='users/logout.html'), name = 'logout' ), #Path to premade django logout module
    path("connect/<str:operation>/<int:pk>/", profile_views.change_friends, name = 'change_friends'),
    path('profile/', profile_views.profile, name='profile'), #Path to profile view
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




