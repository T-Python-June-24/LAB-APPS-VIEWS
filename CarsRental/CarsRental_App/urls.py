from . import views
from django.urls import path

app_name = "CarsRental_App"

urlpatterns = [
    path('', views.home_view, name="home_view"),
    path("about/", views.about_view, name="about_view"),
    path("password/generate/", views.pwGenerator_view, name="pwGenerator_view")
]