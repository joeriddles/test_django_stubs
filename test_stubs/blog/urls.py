from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("", views.cool_posts, name="cool_posts"),
]
