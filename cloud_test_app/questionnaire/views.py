from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from . models import Favourite

import calendar

month_names = [calendar.month_name[i] for i in range(1, 13)]
weekday_names = [calendar.day_name[i] for i in range(7)]

def index(request):
    num_answers = Favourite.objects.count()
    context = {
        'title': "Basic Questions!",
        'num_answers': num_answers,
    }
    return render(request, 'questionnaire/index.html', context)

def questionnaire(request):
    context = {
        'month_names': month_names,
        'weekday_names': weekday_names,
    }
    return render(request, 'questionnaire/questionnaire.html', context)

def results(request):
    return HttpResponse('Results view placeholder. More incoming!')

def answered(request):
    return HttpResponseRedirect(reverse('questionnaire:index'))
