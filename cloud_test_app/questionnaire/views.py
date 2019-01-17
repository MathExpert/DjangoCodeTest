from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

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
    def on_bad_data(request):
        messages.add_message(request, messages.ERROR, 'There was a problem with sent data, please answer again.')
        return HttpResponseRedirect(reverse('questionnaire:questionnaire'))

    # Some checks in case of malicious or erroneous POST request
    try:
        fav_month = int(request.POST['month'])
        fav_weekday = int(request.POST['weekday'])
    except (ValueError, KeyError):
        return on_bad_data(request)

    if fav_month < 1 or fav_month > 12 or fav_weekday < 1 or fav_weekday > 7:
        return on_bad_data(request)

    new_fav = Favourite(fav_month=fav_month, fav_weekday=fav_weekday)
    new_fav.save()

    return HttpResponseRedirect(reverse('questionnaire:index'))
