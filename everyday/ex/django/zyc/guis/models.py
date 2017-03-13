from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class User(AbstractBaseUser):
    points = models.PosivieIntegerField("Score",default=0)

    class Meta(AbstractBaseUser):
        swappable = 'AUTH_USER_MODEL'
