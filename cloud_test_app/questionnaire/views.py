from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from . models import Favourite

def index(request):
    num_answers = Favourite.objects.count()
    context = {
        'title': "Basic Questions!",
        'num_answers': num_answers,
    }
    return render(request, 'questionnaire/index.html', context)

def questionnaire(request):
    return HttpResponse('Questionnaire view placeholder. Wait for it!')

def results(request):
    return HttpResponse('Results view placeholder. More incoming!')

def answered(request):
    return HttpResponseRedirect(reverse('questionnaire:index'))
