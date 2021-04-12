from django.shortcuts import render
from django.http import HttpResponse    
from django.template import loader

from .models import Notify

# Create your views here.
def index(request):
    notifies = Notify.objects.order_by('-pub_date')[:5]
    template  = loader.get_template('home/index.html')

    context = {
        'notifies': notifies,
    }

    return  HttpResponse(template.render(context, request))