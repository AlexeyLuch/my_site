from __future__ import unicode_literals
import datetime
from django.db import models
from django.db.models import TextField
from django.utils import timezone


class Referer(models.Model):
    ref_link = models.CharField(max_length=200)
    describe_link = models.TextField()
    free_test = models.BooleanField(default=True)
    personal_proxy = models.BooleanField(default=True)
    change_proxy = models.BooleanField(default=True)
    public = models.BooleanField(default=True)
    img = models.ImageField(upload_to='img', default='img/q12.jpg')


    def __str__(self):
        return self.describe_link
