from . import views
from django.urls import path

urlpatterns = [
    path('', views.home_view, name="home_view"),
    path("about/", views.about_view, name="about_view"),
    path("password/generate/", views.gen_password, name="gen_password")
]
