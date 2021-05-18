from django.shortcuts import render
from contests.models import Result
def about(request):
    user = request.user
    # print(user)
    list_result = Result.objects.filter(user=user)
    # print(list_result)
    context = {'list_result':list_result}
    return render(request, 'about/about.html', context)
# Create your views here.
