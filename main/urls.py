from . import views
from django.urls import path

#urlpatterns links urls to certain views or functions
urlpatterns = [
    path('', views.index, name='index'), #Index is the homepage and shows an index of all posts on the site
]

