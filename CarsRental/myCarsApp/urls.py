from django.urls import path
from . import views

app_name = 'myCarsApp'
urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about_view, name= "about_view"),
    path("password/generate/",views.generate_password, name= "generate_password"),
]
