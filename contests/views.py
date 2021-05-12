import os

from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect

from .models import Contest, Exercise, Result, Rank


from .forms import UploadDataTrain
from .runcode import run_file_code
from .writefile import handle_upload_file, write_input


def view_contest(request):
    contests = Contest.objects.all()
    for contest in contests:
        __get_user_in_contest(contest)
    context = {
        'list_contest': contests
    }
    return render(request, 'contests/contest.html', context)


def detail(request, contest_id):
    contest = get_object_or_404(Contest, pk=contest_id)
    exercises = contest.exercise_set.all()
    for exercise in exercises:
        __get_user_in_exercise(exercise)
    return render(request, "contests/detail.html", {'contest': contest, 'ex': exercises})
def rank(request, contest_id):
    if request.user is not None:
        contest = get_object_or_404(Contest, pk=contest_id)
        list_exercise = contest.exercise_set.all()
        result_contest = {}
        for exercise in list_exercise:
            list_user = __get_user_in_exercise(exercise)
            for user in list_user:
                result_contest[user]=0

        for exercise in list_exercise:
            list_user = __get_user_in_exercise(exercise)
            for user in list_user:
                user_result=Result.objects.filter(exercise=exercise, user=user)
                max_score = __get_max_score(user_result)
                result_contest[user] +=max_score
        # for result in result_contest:
        #     rank=Rank(contest=contest,user=result.keys)
        context = {'rank':result_contest, 'contest':contest}
        return render(request,'contests/rank.html',context)
    else:
        view_contest(request, contest_id)
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
    print (file)
    file_name = handle_upload_file(file)
    print('file_name', file_name)

    if file_name is None:
        return HttpResponseRedirect('')
    #__show_form_submit(request, exercise_id)

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
    score = count*10
    total_score = total*10
    result = Result(exercise=exercise,user=request.user,score=score,total=total_score)
    result.save()





    return render(request, 'contests/result.html', {'total': total, 'count': count})
def __show_form_submit(request, exercise_id):
    exercise = get_object_or_404(Exercise, pk=exercise_id)
    form = UploadDataTrain()
    return render(request, 'contests/submit_exercise.html', {'exercise': exercise, 'form': form})
    # submit_exercise(request, exercise_id)
def __get_user_in_contest(contest):
    exercises = contest.exercise_set.all()
    list_user = set()
    for exercise in exercises:
        results = Result.objects.filter(exercise=exercise)
        for result in results:
            list_user.add(result.user)
    # print(len(list_user))
    contest.participant = len(list_user)
    contest.save()
    return list_user
def __get_user_in_exercise(exercise):
    results = Result.objects.filter(exercise=exercise)
    list_user=set()
    for result in results:
        list_user.add(result.user)
    exercise.solved = len(list_user)
    exercise.save()
    return list_user
def __get_max_score(user_result):
    max = 0
    for result in user_result:
        if max < result.score:
            max = result.score
    return max