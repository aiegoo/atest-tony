from django.urls import path
from . import views

urlpatterns = [
    path('',
     views.home,
     # views.taskstring,
     # views.taskxml,
     name='View'
    ),
]
