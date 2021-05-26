from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    # name
    name = models.CharField(max_length=128)
    # description
    description = models.TextField(blank=True)
    # posts
    # post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # posts = models.ManyToManyField(Post, blank=True, related_name='categories')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


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
    #category
    categories = models.ManyToManyField(Category, blank=True )
    
    def __str__(self):
        return self.title



