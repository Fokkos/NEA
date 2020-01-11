#Views contains the python code used for functionality within webpages and is used for backend development
from django.shortcuts import render
from django.views import generic
from .models import Post
from django.db.models import Q

def index(request): #Handles the homepage and makes sure it gets rendered correctly
    context = {'posts': Post.objects.filter(status=1).order_by('-published')} #Only shows published objects and orders by date of publication
    return render(request, 'main/index.html', context) #Sends the context to the index template and renders it

def search(request):
    context=0
    query = request.GET.get('q')
    if query:
        context = {'posts': Post.objects\
        .filter(Q(title__icontains=query))\
        #.filter(Q(content__icontains=query))\
        #.filter(Q(tag2__icontains=query))\
        #.filter(Q(tag2__icontains=query))\
        .filter(status=1)\
        .order_by('-published')}
            #status=1,
            #Q(title__icontains="query"),
            #Q(content__icontains="query"),
            #Q(userID__icontains="query"),
            #Q(tag2__icontains="query"),
            #Q(tag2__icontains="query",
        #).order_by('-published')} #Only shows published objects and orders by date of publication
        return render(request, 'main/search.html', context) #Sends the context to the index template and renders it
    else:
        return render(request, "main/noSearchResults.html")
    




        
