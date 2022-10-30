from django.urls import path

from . import views

urlpatterns = [ 
    path('', views.backendTask.as_view()),
]