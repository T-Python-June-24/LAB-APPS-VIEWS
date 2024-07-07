from django.urls import path
from . import views
app_name="main"
urlpatterns = [
    path('', views.welcome_page,name='welcome_page'),
    path('about/', views.about_page,  name='about_page'),
    path('password/generate/', views.password_page,name='password_page')

]
