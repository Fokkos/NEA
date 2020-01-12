#Views contains the python code used for functionality within webpages and is used for backend development
from django.shortcuts import render
from django.views import generic
from .models import Post
from django.db.models import Q

def index(request): #Handles the homepage and makes sure it gets rendered correctly
    context = {'posts': Post.objects.filter(status=1).order_by('-published')} #Only shows published objects and orders by date of publication
    return render(request, 'main/index.html', context) #Sends the context to the index template and renders it

def search(request): #Handles how searches work on my website
    query = request.GET.get('q') #uses request.GET to get the search term, defined by URL variable "q"
    if query: #If there a search was made (i.e. if a q value is in the url)
        context = {'posts': Post.objects.filter(Q(title__icontains=query) |\
             Q(content__icontains=query))\
            .filter(status=1)\
            .order_by('-published')}
        return render(request, 'main/search.html', context) #Sends the context to the index template and renders it
    else:
        return render(request, "main/initialSearch.html")
    




        
