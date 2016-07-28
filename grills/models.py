from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Grill(models.Model):
    """
    'You misogynistic degenerate! This is awful!'
    """
    trap = models.BooleanField()
    meme_lord = models.BooleanField()
    higher_up = models.BooleanField()
    name = models.CharField(max_length=32)
    twitter = models.CharField(max_length=72)
    description = models.TextField(max_length=140)
    poster = models.ForeignKey(User)
