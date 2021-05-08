import os

from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from .models import Contest, Exercise
from .forms import UploadDataTrain
from .runcode import run_file_code
from .writefile import handle_upload_file, write_input


def view_contest(request):
    contests = Contest.objects.all()
    context = {
        'list_contest': contests
    }
    return render(request, 'contests/contest.html', context)


def detail(request, contest_id):
    contest = get_object_or_404(Contest, pk=contest_id)
    exercises = contest.exercise_set.all()
    return render(request, "contests/detail.html", {'contest': contest, 'ex': exercises})


def view_exercise(request, exercise_id):
    if request.method == 'POST':
        # check validation
        if not request.user.is_authenticated:
            return HttpResponse('Unauthorized', status=401)

        form = UploadDataTrain(request.POST, request.FILES)

        if form.is_valid():
            return __submit_code(request, exercise_id)
    else:
        return __show_form_submit(request, exercise_id)


def __submit_code(request, exercise_id):
    file = request.FILES['file']
    file_name = handle_upload_file(file)
    print('file_name', file_name)

    exercise = get_object_or_404(Exercise, pk=exercise_id)

    list_testcase = exercise.testcase_set.all()
    total = len(list_testcase)
    count = 0

    for testcase in list_testcase:
        print('testcase', testcase.input)
        file_input = write_input(testcase.input)
        print('file_input', file_input)

        try:
            output = run_file_code(file_name, file_input)
            print('output', output)
            output_test = str(testcase.output).strip()
            print(output_test)

            if output == output_test:
                count += 1
        except Exception as e:
            print(e)

        # remove file input
        os.remove(file_input)

    # remove file code
    os.remove(file_name)

    return render(request, 'contests/result.html', {'total': total, 'count': count})


def __show_form_submit(request, exercise_id):
    exercise = get_object_or_404(Exercise, pk=exercise_id)
    form = UploadDataTrain()
    return render(request, 'contests/submit_exercise.html', {'exercise': exercise, 'form': form})
    submit_exercise(request, exercise_id)
