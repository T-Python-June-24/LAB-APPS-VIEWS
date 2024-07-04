

from . import views
from django.urls import path


urlpatterns = [
    path("", views.home_view),
    path("about/", views.about_view),
    path("password/generate/", views.pass_generator)
]