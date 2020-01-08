#Views contains the python code used for functionality within webpages and is used for backend development
from django.shortcuts import render
from django.views import generic
from .models import Post

def index(request): #Handles the homepage and makes sure it gets rendered correctly
    context = {'posts': Post.objects.filter(status=1).order_by('-published')} #Only shows published objects and orders by date of publication
    return render(request, 'main/index.html', context) #Sends the context to the index template and renders it


