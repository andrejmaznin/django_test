from django.conf import settings
from django.db import models
from django.utils import timezone


class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    tags = models.TextField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
