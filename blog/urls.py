from django.urls import path
from . import views


urlpatterns = [
    path("", views.blog_view, name="blog"),
    path("single-<int:pid>/", views.blog_single, name="single"),
]
