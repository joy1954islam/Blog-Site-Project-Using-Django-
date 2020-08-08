from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    Title = models.CharField(max_length=100)
    content = models.TextField()
    data_posted = models.DateTimeField(default=timezone.now)
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Title