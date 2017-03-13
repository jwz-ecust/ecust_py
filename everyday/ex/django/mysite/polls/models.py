from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Polls(models.Model):
    title = models.CharField(max_length=200)
    catagory = models.CharField(max_length=50,blank=True)
    date_time = models.DateField(auto_now=True)
    content = models.TextField(blank=True,null=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']



class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title