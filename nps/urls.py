from django.urls import path

from nps import views

app_name = 'nps'

urlpatterns = [
    path('', views.home),
    path('debug', views.home2),
]