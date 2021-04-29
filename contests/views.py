from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.
from .models import Contest, Exercise
from .forms import UploadDataTrain

from pathlib import Path


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
    if request.method == 'POST':
        form = UploadDataTrain(request.POST, request.FILES)

        if form.is_valid():
            # print(request.user.username)
            handle_upload_file(request.FILES['file'])
            return HttpResponse("hello")
    else:
        form = UploadDataTrain()
    return render(request, 'contests/submit_exercise.html', {'exercise': exercise,'form':form})

def handle_upload_file(file):
    path = Path(__file__)
    root_path = str(path.parent.parent)+'/storage/'
    with open(root_path + str(file),'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)



