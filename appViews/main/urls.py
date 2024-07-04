from django.urls import path
from . import views
app_name = "name"
urlpatterns = [
    path("about/",views.about_view,name="about_view"),
    path('password/generate/',views.password_view,name="password_view"),
    path('',views.home_view,name="home_view")

]