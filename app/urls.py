
from . import views
from django.urls import path

urlpatterns = [
    path("", views.CryptoView.as_view(), name="crypto_view")
]
