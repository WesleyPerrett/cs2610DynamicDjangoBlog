from django.db import models
from django.utils import timezone

import datetime

class Blog(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    content = models.TextField()
    posted = models.DateTimeField('date posted')

    # def __str__(self):
    #     return self.title

    # def __str__(self):
    #     return self.author

    # def __str__(self):
    #     return self.content
    
    # def posted_date(self):
    #     return self.posted

class Comments(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    commenter = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    content = models.TextField()
    posted = models.DateTimeField('date posted')
        
    # def __str__(self):
    #     return self.commenter

    # def __str__(self):
    #     return self.email

    # def __str__(self):
    #     return self.content
    
    # def posted_date(self):
    #     return self.posted
    
class About(models.Model):
    current_date = models.DateTimeField('current date')