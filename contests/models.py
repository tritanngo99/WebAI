from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Contest(models.Model):
    name = models.CharField(max_length=256)
    contest_type = models.CharField(max_length=20)
    start = models.DateTimeField('date-published')
    length = models.DurationField()
    status = models.CharField(max_length=20)
    participant = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    def get_status(self):
        subtime = self.start - timezone.now()
        if subtime.days > 0:
            return "Before start {}".format(subtime.days) +" day"
        elif subtime.days == 0 :
            return "Before start {}".format(subtime)
        else :
            subtime = timezone.now() - self.start
            if subtime < self.length:
                return "After end {}".format(subtime)
            return "Final standings"

    # def get_participant(self):
    #     exercises = self.exercise_set.all()
    #     count = 0
    #     for exercise in exercises:
    #
class Exercise (models.Model):
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

class Result(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()