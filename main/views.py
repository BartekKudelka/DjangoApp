from django.shortcuts import render
from .models import Event
from django.contrib.auth.decorators import login_required


def show_event(request):
    return render(request, 'window1.html')


def show_profile(request):
    return render(request, 'profile.html')
# Create your views here.
