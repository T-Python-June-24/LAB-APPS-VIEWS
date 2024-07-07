from django.urls import path
from . import views

app_name = "home"
urlpatterns = [
    path('', views.welcome_view, name='welcome_view'),
    path('about/', views.about_view, name='about_view'),
    path('password/generate/', views.generate_password, name='generate_password'),

]
