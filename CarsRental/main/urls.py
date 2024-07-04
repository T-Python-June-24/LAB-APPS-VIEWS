from django.urls import path 
from . import views
app_name = "name"


urlpatterns = [
  path("", views.page_view, name="page_view"),
  path("about/", views.about_view, name="about_view"),
  path("password/generate/", views.password_generator_view, name="password_generate_view")
]