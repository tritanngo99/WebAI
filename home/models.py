import datetime

from django.db import models
from django.utils import timezone

class Notify(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    pub_date = models.DateField(default=timezone.now)
    def __str__(self):
        return self.title