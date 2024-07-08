from django.urls import path, include
from . import views

app_name = 'main'


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('password/generate/', views.generate_password, name='generate_password'),
]
