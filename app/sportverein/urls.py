from django.urls import path
from . import views

# Hier wird eingestellt, welche urls es auf der Seite gibt.
urlpatterns = [
    path('', views.index, name='index'),
    path('forms/', views.sportform, name="form")
]
