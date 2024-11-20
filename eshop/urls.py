from django.urls import path
from . import views


urlpatterns = [
    path ('pozdrav', views.index, name='index')
]

