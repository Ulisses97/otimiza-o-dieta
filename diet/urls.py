from django.urls import path
from diet import views


urlpatterns = [path("", views.index, name="index"), path("criarDieta", views.criarDieta)]
