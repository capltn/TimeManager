"""Module to link basic urls."""

from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.tcm_user_register, name="register_user"),
    path("login/", views.tcm_user_login, name="login_user"),
    path("logout/", views.tcm_user_logout, name="logout_user"),
]
