#models.py is used to display all models created for databases
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

#Status is used to display whether a post is published or still in the drafts
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

#Tags is used to attribute different definitions to posts which cover genre and speed, used for categorisation purposes
TAGS = (
    (0,"None"),
    (1,"Alt-Rock"),
    (2,"Blues"),
    (3,"Classical"),
    (4,"Country"),
    (5,"Dance"),
    (6,"Drum and Bass"),
    (7,"Dubstep"),
    (8,"Easy listening"),
    (9,"Electro"),
    (10,"Emo"),
    (11,"Eurobeat"),
    (12,"Experimental"),
    (13,"Fast"),
    (14,"Folk"),
    (15,"Funk"),
    (16,"Garage"),
    (17,"Grime"),
    (18,"Grunge"),
    (19,"Hip Hop"),
    (20,"Indie"),
    (21,"Jazz"),
    (22,"Latin"),
    (23,"Lo-Fi"),
    (24,"Metal"),
    (25,"Motown"),
    (26,"Mod"),
    (27,"Opera"),
    (28,"Pop"),
    (29,"Prog Rock"),
    (30,"Punk"),
    (31,"R&B"),
    (32,"Rap"),
    (33,"Reggae"),
    (34,"Rock"),
    (35,"Slow"),
    (36,"Soul"),
    (37,"Techno"),
    (38,"Trance"),
    (39,"Trip-Hop")
)

#Model used to store all data regarding blog posts
class Post(models.Model): #Defines the class as a model
    title = models.CharField(max_length=50, unique=True) #The title of the post
    slug = models.SlugField(max_length=50, unique=True) #URL Friendly title. Has to be unique to stop collisions when searching for posts via url
    userID = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts') #Defines who created the post
    updated = models.DateTimeField(auto_now= True) #When the post was last updated / changed
    content = models.TextField() #Displays the actual content of the post
    summary = models.CharField(max_length=100, default = "blog post")
    published = models.DateTimeField(auto_now_add=True) #Holds the date and time when the post was first published (used for ordering)
    status = models.IntegerField(choices=STATUS, default=0) #Whether the post has been published or is still being drafted
    media = models.BooleanField(default=True) #Whether the post has media or not
    #Below 2 fields are used to define the tags that the posts have attributed to them. Allows for better catgorisation and analysis
    tag1 = models.IntegerField(choices=TAGS, default="none")
    tag2 = models.IntegerField(choices=TAGS, default="none")

    class Meta:
        ordering = ['-published'] #Defines the ordering of the data, which is by the date it was published (newest first)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("feed") #Redirects user back to feed once a post is created!


        
    