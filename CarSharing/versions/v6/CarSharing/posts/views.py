from django.shortcuts import render
from django.shortcuts import render_to_response,RequestContext
# from posts.models import WeatherData
# from weather_app.forms import CarSharingForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect


def welcome(request):
    return render(request,'welcome.html')


