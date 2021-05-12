from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone






class Contest(models.Model):
    name = models.CharField(max_length=256)
    contest_type = models.CharField(max_length=20)
    start = models.DateTimeField('date-published')
    length = models.DurationField()
    participant = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_status(self):
        timeend = self.start + self.length
        if timeend <= timezone.now():
            return "Final standings"
        elif self.start <= timezone.now():
            subtime = timeend - timezone.now()
            return 'After end {}'.format(subtime)
        else:
            subtime = self.start - timezone.now()
            if subtime.days > 0:
                return 'Before start {} {}'.format(subtime.days, 'day')
            elif subtime.days == 0:
                return 'Before start {}'.format(subtime)


class Exercise(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    solved = models.IntegerField(default=0)
    time_limit = models.IntegerField()
    memory_limit = models.IntegerField()
    description = models.TextField()
    input = models.TextField()
    output = models.TextField()

    def __str__(self):
        return self.name


class TestCase(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    input = models.TextField()
    output = models.TextField()

    def __str__(self):
        return 'Test Case {} {}'.format(self.exercise, self.id)

class Result(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    total = models.IntegerField(default=100)

    def __str__(self):
        result = '{} {} {}/{}'.format(self.exercise.name,self.user.username,self.score,self.total)
        return result

class Rank(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
