from django.db import models

class Notify(models.Model):
    content = models.CharField(max_length=1024)
    pub_date = models.DateTimeField('date published')
