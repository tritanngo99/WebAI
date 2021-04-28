from django.db import models
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
            print(subtime)
            if subtime < self.length:
                return "After end {}".format(subtime)
            return "Final standings"
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