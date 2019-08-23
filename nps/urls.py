from django.urls import path

from nps import views

app_name = 'nps'

urlpatterns = [
    path('debug', views.home),
    path('', views.home2),
]