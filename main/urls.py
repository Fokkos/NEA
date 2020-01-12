from . import views
from django.urls import path
from .views import viewPost

#urlpatterns links urls to certain views or functions
urlpatterns = [
    path('', views.index, name='index'), #Index is the homepage and shows an index of all posts on the site
    path('search/', views.search, name='search'), #URL for the search functionality of the site
    path('<str:userID>/post/<slug:slug>/', viewPost.as_view(), name = 'post-detail'), #URL for individual posts
]

