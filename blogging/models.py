from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    #title
    title = models.CharField(max_length=128)
    #text / body
    text = models.TextField(blank=False)
    #author
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #created_date
    created_date = models.TimeField(auto_now_add=True)
    #modified_date
    modified_date = models.TimeField(auto_now=True)
    #published_date
    published_date = models.TimeField(blank=True, null=True)
    
    def __str__(self):
        return self.title