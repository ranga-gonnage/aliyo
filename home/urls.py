from django.urls import path

from home import views

app_name = "home"
urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("mentions-legales/", views.LegalNotice.as_view(), name="legalNotice"),
    path("politique-de-confidentialite/", views.PrivacyPolicy.as_view(), name="privacyPolicy"),
]