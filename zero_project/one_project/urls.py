# app_blog/urls.py
from django.urls import path
from one_project import views

urlpatterns = [
    path(r'', views.HomePageView.as_view()),
]
