from django.urls import path

from solutions import views

app_name = "solutions"
urlpatterns = [
    path("creer-un-site-web/", views.WebSite.as_view(), name="website"),
    path("creer-une-application-mobile/", views.MobileApp.as_view(), name="mobileApp"),
]