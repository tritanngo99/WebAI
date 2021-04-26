from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.
from .models import Contest, Exercise


def view_contest(request):

    contests = Contest.objects.all()

    context = {
        'list_contest' : contests
    }
    return render(request, 'contests/contest.html',context)
def detail(request, contest_id):
    contest = get_object_or_404(Contest, pk = contest_id)
    exercise = contest.exercise_set.all()
    return render(request, "contests/detail.html",{'contest':contest,'ex':exercise})


def submit_exercise(request, exercise_id):
    exercise = get_object_or_404(Exercise, pk=exercise_id)
    return render(request, 'contests/submit_exercise.html', {'exercise': exercise})