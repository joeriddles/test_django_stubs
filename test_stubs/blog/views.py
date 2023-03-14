from django.http import HttpRequest
from django.shortcuts import render

from . import models


def cool_posts(request: HttpRequest):
    posts = models.Post.objects.cool()
    return render(request, "blog/posts.html", {"posts": posts})
