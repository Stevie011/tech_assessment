from django.urls import path

from .views import home_page_view

urlpatterns = [
    #This sends us to the home view
    path("", home_page_view, name="home"),
]