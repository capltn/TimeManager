"""Module for all user views."""

from django.http import HttpRequest, HttpResponse
from tcm_user.logic import handle_user_request


def tcm_user_register(request: HttpRequest) -> HttpResponse:
    """Handle incoming home screen request."""
    return handle_user_request.handle_user_register_view(request)


def tcm_user_login(request: HttpRequest) -> HttpResponse:
    """Handle incoming login request."""
    return handle_user_request.handle_user_login(request)


def tcm_user_logout(request: HttpRequest) -> HttpResponse:
    """Handle incoming logout request."""
    return handle_user_request.handle_user_logout(request)
