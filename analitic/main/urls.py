from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('relevance', views.relevance),
    path('geography', views.geography),
    path('skills', views.skills),
    path('last_vacancies', views.last_vacancies)
]
