from django.urls import path
from . import views

app_name ="CarsRental"

urlpatterns =[
    path("", views.page_view, name="contacts"),
    path("about/", views.about_view, name="booking"),
    path("password/generate/", views.password_view, name="profile"),
]