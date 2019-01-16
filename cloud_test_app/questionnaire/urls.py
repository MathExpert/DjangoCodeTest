from django.urls import path

from questionnaire import views

app_name = 'questionnaire'
urlpatterns = [
    path('', views.index, name="index"),
    path('questionnaire', views.questionnaire, name='questionnaire'),
    path('results', views.results, name='results'),
    path('answered', views.answered, name='answered'),
]
