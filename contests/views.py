import os

from django.shortcuts import render, get_object_or_404

from .models import Contest, Exercise, TestCase
from .forms import UploadDataTrain
from .runcode import solve
from .writefile import handle_upload_file, write_input
from .removefile import remove_file_in_storage
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
    form = UploadDataTrain()
    return render(request, 'contests/submit_exercise.html', {'exercise': exercise,'form':form})

def submit_and_run(request, exercise_id):
    if request.method == 'POST':
        form = UploadDataTrain(request.POST, request.FILES)
        if form.is_valid():
            # print(request.user.username)
            handle_upload_file(request.FILES['file'])
            file_name = str(request.FILES['file'])
            file_run = './storage/' + file_name
            exercise = get_object_or_404(Exercise, pk=exercise_id)
            path = Path(__file__)
            list_testcase = exercise.testcase_set.all()
            result=''
            for testcase in list_testcase:
                print(testcase.input)
                write_input(testcase.input)
                output_code = str(solve(file_run)).rsplit()
                print(output_code)
                output_test = str(testcase.output).rsplit()
                print(output_test)
                if (output_code==output_test):
                    result = 'success'
            # remove_file(file_name)
            return render(request, 'contests/result.html', {'output':result})
    else:
        submit_exercise(request, exercise_id)