from . import views
from django.urls import path
from .views import viewPost, createPost, editPost, deletePost, postIndex, viewUser, Feed, userIndex

#urlpatterns links urls to certain views or functions
urlpatterns = [
    path('posts/', postIndex.as_view(), name = "post-index"), #Index is the homepage and shows an index of all posts on the site
    path('users/', userIndex.as_view(), name = "user-index"), #Index is the homepage and shows an index of all users on the site
    path('search/', views.search, name='search'), #URL for the search functionality of the site
    path('user_search/', views.userSearch, name='user-search'), #URL for the user search functionality of the site
    path('<str:userID>/post/<slug:slug>/', viewPost.as_view(), name = 'post-detail'), #URL for individual posts
    path('create/',createPost.as_view(), name='post-create'), #URL for post creation
    path('<str:userID>/post/<slug:slug>/edit/', editPost.as_view(), name = 'post-update'), #URL for updating posts
    path('<str:userID>/post/<slug:slug>/delete/', deletePost.as_view(), name = 'post-delete'), #URL for updating posts
    path('user/<str:username>/', viewUser.as_view(), name='user-posts'), #URL for custom user profiles
    path("", Feed.as_view(), name = "feed"),
]


