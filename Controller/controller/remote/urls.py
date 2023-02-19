from django.urls import path, include
from .views import helloAPI , checkAPI , registerMachine

urlpatterns = [
    path("hello/",helloAPI),
    path("test/", checkAPI),
    path("register/",registerMachine)
]