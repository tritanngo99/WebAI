from django.shortcuts import render, get_object_or_404
from .models import Notify


def index(request):
    # get 10 notifies newest
    notifies = Notify.objects.order_by('pub_date')[:10]
    context = {
        'notifies': notifies
    }
    return render(request, 'home/index.html', context)


def detail(request, notify_id):
    notify = get_object_or_404(Notify, pk=notify_id)
    return render(request, 'home/detail.html', {'notify': notify})
