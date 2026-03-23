from django.shortcuts import render
from django.http import HttpRequest,    HttpResponse, JsonResponse
from django.urls import NoReverseMatch, reverse


def home_view(request: HttpRequest) -> HttpResponse:
    """Return home screen."""
    return render(request, "base/home.html")

def link_request(request: HttpRequest) -> HttpResponse:
    """Return requested link."""
    if request.method != "GET":
        return JsonResponse({"error": "Invalid request"}, status=422)
    link_identifier = request.GET.get("linkid")
    primary_key = request.GET.get("pk")
    args = [] if primary_key == "undefined" else [primary_key]
    try:
        resolved_url = reverse(link_identifier,args=args)
        return JsonResponse({"resolved_url": resolved_url}, status=200)
    except NoReverseMatch:
        return JsonResponse({"error": "Invalid request"}, status=422)