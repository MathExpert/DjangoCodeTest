from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.db.models import Count

from . models import Favourite

import calendar
from collections import OrderedDict

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
    # Database contents in a real situation might be big, so
    # instead of reading up all the contents and processing them in
    # Python, I query the database.

    def get_entries_with_count(query_set, field_name):
        return query_set.order_by(field_name).annotate(fav_count=Count(field_name))

    def get_dict_with_count(query_set, field_name):
        result = OrderedDict()
        for fav in query_set:
            result[fav[field_name]] = fav['fav_count']
        return result

    def prepare_fav_data(field_name, names):
        values = Favourite.objects.values(field_name)
        count_entries = get_entries_with_count(values, field_name)
        fav_counts = get_dict_with_count(count_entries, field_name)
        total = values.count()
        return [(names[k - 1], v, '{0:.2f}'.format(100 * v / total)) for k, v in fav_counts.items()]

    fav_month_data = prepare_fav_data('fav_month', month_names)
    fav_weekday_data = prepare_fav_data('fav_weekday', weekday_names)

    fav_relative_data = []
    # There should be a more elegant way to query this data,
    # but my SQL knowledge is limited so far.
    for i in range(1, 12):
        field_name = 'fav_weekday'
        weekday_values = Favourite.objects.filter(fav_month=i).values(field_name)
        if weekday_values.count() == 0:
            continue
        weekday_counts = get_entries_with_count(weekday_values, field_name)
        fav_weekday = weekday_counts.latest('fav_count')['fav_weekday']

        fav_relative_entry = (month_names[i - 1], weekday_names[fav_weekday - 1])
        fav_relative_data.append(fav_relative_entry)

    context = {
        'fav_month_data': fav_month_data,
        'fav_weekday_data': fav_weekday_data,
        'fav_relative_data': fav_relative_data,
    }

    return render(request, 'questionnaire/results.html', context)

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
