from . import views
from django.urls import path

app_name = 'abdullahApp'
urlpatterns = [
    path('', views.homePage, name='home'),
    path('about/', views.aboutPage, name='about'),
    path('password/generate/', views.passwordPage, name='password_generate'),
    path('langchain/', views.process_csv_data, name='process_csv_data'),
]