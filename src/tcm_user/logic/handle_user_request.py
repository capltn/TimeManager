"""Module to handle different incoming request."""

from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse

from tcm_user.forms import CreateUserForm, LoginForm
from tcm_user.models import TCMProfile
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth


def user_register_get(request: HttpRequest, form: CreateUserForm) -> HttpResponse:
    """Return the registration page based on the given form."""
    context = {"registerform": form}
    if form.errors:
        context["hint"] = next(iter(form.errors.values()))[0]
    return render(request, "tcm_user/register.html", context=context)


def handle_user_register_view(request: HttpRequest) -> HttpResponse:
    """Handle user registration."""
    # Return registration form surface
    if request.method != "POST":
        return user_register_get(request, CreateUserForm())

    form = CreateUserForm(request.POST)
    # Handle invalid registration try
    if not form.is_valid():
        return user_register_get(request, form)

    # Save the new user and created the associated TCMProfile
    created_user = form.save()
    TCMProfile.objects.create(user=created_user)
    return redirect("home")


def handle_user_login(request: HttpRequest) -> HttpResponse:
    """Login a user."""
    if request.method != "POST":
        return render(request, "tcm_user/login.html", context={"loginform": LoginForm()})

    form = LoginForm(request, data=request.POST)
    if form.is_valid():
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("home")
    return render(request, "tcm_user/login.html", context={"loginform": form})


def handle_user_logout(request: HttpRequest) -> HttpResponse:
    """Logout a user."""
    auth.logout(request)
    return redirect("login_user")
