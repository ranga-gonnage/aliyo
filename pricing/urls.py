from django.urls import path

from pricing import views

app_name = "pricing"
urlpatterns = [
    path("tarifs/", views.Pricing.as_view(), name="pricing"),
]