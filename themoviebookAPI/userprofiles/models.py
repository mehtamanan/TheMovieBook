from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name = 'profile')
    bio = models.TextField(blank = True, null = True)
    birth_date = models.DateField(blank = True, null = True)
    following = models.ManyToManyField('self', related_name = 'followers', symmetrical=False)

    def __unicode__(self):
        return self.user.username
    
class Post(models.Model):
    owner = models.ForeignKey(UserProfile, related_name = 'post')
    movie_title = models.CharField(max_length = 200)
    movie_id = models.CharField(max_length = 20)
    caption = models.CharField(max_length = 200)
    upload_date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.movie_title
