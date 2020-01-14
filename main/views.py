#Views contains the python code used for functionality within webpages and is used for backend development
from django.shortcuts import (
    render, #Used to render templates
    get_object_or_404 #Used to render custom 404 pages
) 
from django.views import generic 
from django.contrib.auth.models import User #Imports the user model
from .models import Post #Imports all of the blog posts
from users.models import Profile #Imports user profile (extension to user model)
from django.db.models import Q #To make queries
from django.contrib.auth.mixins import (
    LoginRequiredMixin, #@Login.Required equivalent for class based views
    UserPassesTestMixin #Checks to see if current user is the correct user
)
from django.views.generic import (
    ListView, #Used when creating a page containing a list of objects
    DetailView, #Used when making a more detailed page for each blog post
    CreateView, #Used when making a form for users to create blog posts
    UpdateView, #Used so that a user can update a post they have posted
    DeleteView  #Used so that a user can delete a post they have posted
)

class index(ListView): #Defines the main page of the website (the index)
    model = Post #Defines the model used for this class as the Post model
    template_name = 'main/index.html' #Ensures that the template used is the index.html template
    queryset = Post.objects.filter(status=1)  #Filters objects by whether they have been published
    context_object_name = 'posts' #Defines how the model used will be referred to as in the template
    ordering = ['-published'] #Orders posts by newest first
    paginate_by = 10 #Displays 10 posts per page

class viewUser(ListView): #Defines the main page of the website (the index)
    model = Post #Defines the model used for this class as the Post model
    template_name = 'main/user_posts.html' #Ensures that the template used is the index.html template
    context_object_name = 'posts' #Defines how the model used will be referred to as in the template
    paginate_by = 10 #Displays 10 posts per page

    def get_queryset(self): #Function to check if the user actually exists
        user = get_object_or_404(User, username=self.kwargs.get('username')) #If a user with the username in the URL exists, continue
        return Post.objects.filter(userID=user).filter(status=1).order_by("-published")
    

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

class createPost(LoginRequiredMixin, CreateView): #Class which defines how posts are created
    model = Post
    fields = ['title', 'slug','content','summary','status','tag1','tag2'] #Fields that can be edited by user
    def form_valid(self, form): 
        form.instance.userID = self.request.user #Defines the userID for the post as the ID of the current user
        return super().form_valid(form) #Returns this value to the form

class editPost(LoginRequiredMixin, UserPassesTestMixin, UpdateView): #Class which defines how posts are edited
    model = Post
    fields = ['title', 'slug','content','summary','status','tag1','tag2'] #Fields that can be edited by user
    def form_valid(self, form): 
        form.instance.userID = self.request.user #Defines the userID for the post as the ID of the current user
        return super().form_valid(form) #Returns this value to the form
    def test_func(self): #Used to check if the current user is the author of the post
        currentPost = self.get_object() #Assigns the current post to "currentPost"
        if self.request.user == currentPost.userID: #Checks author of current post to logged in user, if the same...
            return True #User is let in to the page
        else: #Otherwise...
            return False #They are rejected from the page.

class deletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView): #Defines how posts can be deleted
    model = Post
    success_url='/'
    def test_func(self): #Used to check if the current user is the author of the post
        currentPost = self.get_object() #Assigns the current post to "currentPost"
        if self.request.user == currentPost.userID: #Checks author of current post to logged in user, if the same...
            return True #User is let in to the page
        else: #Otherwise...
            return False #They are rejected from the page.
    
           



        
