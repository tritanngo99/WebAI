from django.shortcuts import render
from .models import Notify


def index(request):
    # get 10 notifies newest
    notifies = Notify.objects.order_by('pub_date')[:10]
    context = {
        'notifies': notifies
    }
    return render(request, 'home/index.html', context)
