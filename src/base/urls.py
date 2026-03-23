"""Module to link basic urls."""

from django.urls import path

from base import views

urlpatterns = [path("", views.home_view, name="home"), path("link_resolve/", views.link_request, name="link_request")]
