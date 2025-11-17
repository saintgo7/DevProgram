from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('template/', views.hello_template, name='hello_template'),
]
