from django.urls import path

from .views import home_view

urlpatterns = [
    #This sends us to the home view
    path("", home_view, name="home"),
]