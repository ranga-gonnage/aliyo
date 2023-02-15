from django.urls import path

from contact import views

app_name = "contact"
urlpatterns = [
    path("contact/", views.Contact.as_view(), name="contact"),
    path("a-propos/", views.About.as_view(), name="about"),
]