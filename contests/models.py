from django.db import models

class Contest(models.Model):
    name = models.CharField(max_length=256)
    contest_type = models.CharField(max_length=20)
    start = models.DateTimeField('date-published')
    length = models.DurationField()
    status = models.CharField(max_length=20)
    participant = models.IntegerField()
    def __str__(self):
        return self.name

class Exercise (models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    solved = models.IntegerField()
    time_limit = models.IntegerField()
    memory_limit = models.IntegerField()
    description = models.TextField()
    input = models.TextField()
    output = models.TextField()

    def __str__(self):
        return self.name
