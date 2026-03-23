"""Module for all user views."""

from django.http import HttpRequest, HttpResponse
from tcm_user.logic.handle_user_request import handle_user_register_view


def tcm_user_register(request: HttpRequest) -> HttpResponse:
    """Return home screen."""
    return handle_user_register_view(request)
