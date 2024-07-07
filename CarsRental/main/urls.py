

from . import views
from django.urls import path

app_name = 'main'


urlpatterns = [
    path("", views.home_view, name= 'home'),
    path("about/", views.about_view, name= 'aboutUs'),
    path("password/generate/", views.pass_generator, name= 'passGen')
]