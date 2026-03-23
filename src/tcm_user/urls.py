"""Module to link basic urls."""

from django.urls import path

from . import views

urlpatterns = [path("register/", views.tcm_user_register, name="register_user")]
