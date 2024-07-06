from django.urls import path
from . import views
urlpatterns = [
    path('', views.welcome_page,name='welcome_view'),
    path('about/', views.about_page,  name='welcome_view'),
    path('password/generate/', views.password_page,name='password_page')

]
