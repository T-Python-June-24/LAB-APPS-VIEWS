from django.urls import path
from . import views

urlpatterns= [
    path("", views.homepage, name="homepage"),
    path("about/", views.aboutpage, name="aboutpage"),
    path("password/generate", views.password_generate, name="password_generate")
]

