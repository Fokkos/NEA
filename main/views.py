#Views contains the python code used for functionality within webpages and is used for backend development
from django.shortcuts import render #Used to render templates
from django.views import generic 
from .models import Post #Imports all of the blog posts
from django.db.models import Q #To make queries
from django.views.generic import (
    DetailView, #Used when making a more detailed page for each blog post
    CreateView #Used when making a form for users to create blog posts
)


def index(request): #Handles the homepage and makes sure it gets rendered correctly
    context = {'posts': Post.objects.filter(status=1).order_by('-published')} #Only shows published objects and orders by date of publication
    return render(request, 'main/index.html', context) #Sends the context to the index template and renders it

def search(request): #Handles how searches work on my website
    query = request.GET.get('q') #uses request.GET to get the search term, defined by URL variable "q"
    if query: #If there a search was made (i.e. if a q value is in the url)...
        #below code: filters using the Q lookup of if a post title or contents contain the query itself, also filters by if published or not
        context = {'posts': Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query)).filter(status=1).order_by('-published')}
        return render(request, 'main/search.html', context) #Sends the filtered context to the index template and renders it
    else: #If there was no search made...
        return render(request, "main/initialSearch.html") #Take user to a template displaying that it is the initial search

class viewPost(DetailView): #class which defines how individual posts are displayed
    model = Post

class createPost(CreateView): #Class which defines how posts are created
    model = Post
    fields = ['title', 'slug','content','summary','status','tag1','tag2'] #Fields that can be edited by user
    def form_valid(self, form):
        form.instance.userID = self.request.user
        return super().form_valid(form)






        
