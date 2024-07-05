from django.urls import path
from . import views

app_name = 'myCarsApp'
urlpatterns = [
    path("", views.main_view, name="main_view"),
    path("about/", views.about_view, name= "about_view"),
    path("password/generate/",views.generate_password, name= "generate_password"),
]
