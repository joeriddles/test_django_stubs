from __future__ import annotations
from django.db import models

from . import managers


class Post(models.Model):
    title = models.CharField(max_length=256)
    objects = managers.PostQuerySet.as_manager()
