from django.urls import path

from challenges.views import monthly_challenge, monthly_challenge_by_number, index

urlpatterns = [
    path('', index, name='index'),
    path('<int:month>', monthly_challenge_by_number),
    path('<str:month>', monthly_challenge, name='month-challenge'),
]
