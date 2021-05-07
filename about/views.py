from django.shortcuts import render
from .forms import ContestForm

def about(request):
    form = ContestForm()
    form = ContestForm()
    return render(request, 'about/about.html', {'form':form})
# Create your views here.
