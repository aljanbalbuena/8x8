from django.urls import path

from .views import DisplayView

urlpatterns = [
    path(
        "doc/<str:doc_id>/sheet/<str:sheet_id>/",
        DisplayView.as_view(),
    ),
    path(
        "doc/<str:doc_id>/",
        DisplayView.as_view(),
    ),
]
