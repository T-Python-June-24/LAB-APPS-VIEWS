from . import views
from django.urls import path

app_name ="main"
urlpatterns = [
    path('' , views.index_website,name="index_website"),
    path("about/" , views.about , name="about"),
    path("password/generate/" , views.password_generate , name="password_generate")
    
    
]