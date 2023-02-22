from django.urls import path, include
from .views import helloAPI , checkAPI , registerMachine, automodeON, automodeOFF, edge2fog, fog2edge

urlpatterns = [
    path("hello/",helloAPI),
    path("test/", checkAPI),
    path("register/",registerMachine),
    path("autoon/",automodeON),
    path("autooff/",automodeOFF),
    path("e2f/",edge2fog),
    path("f2e/",fog2edge),
]