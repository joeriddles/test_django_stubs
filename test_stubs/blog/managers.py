from django.db import models



class PostQuerySet(models.QuerySet):
    def cool(self):
        return self.filter(title__icontains="cool")
