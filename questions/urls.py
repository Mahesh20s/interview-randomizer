from django.urls import path
from . import views

urlpatterns = [
    path("random/", views.random_question, name="random_question"),
]