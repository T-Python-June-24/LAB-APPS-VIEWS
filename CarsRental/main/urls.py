from django.urls import path
from . import views

app_name ="main"

urlpatterns =[
    path("", views.page_view, name="home"),
    path("about/", views.about_view, name="about"),
    path("contact/", views.contact_view, name="contact"),
    path("password/generate/", views.password_view, name="password"),
    path("cars/", views.cars_view, name="cars"),
    ]