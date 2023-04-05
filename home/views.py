from django.shortcuts import render
from django.views import View

class Home(View):
    def get(self, request):
        context = {}
        return render(request, "home.html", context)

class LegalNotice(View):
    def get(self, request):
        context = {}
        return render(request, "legalNotice.html", context)

class PrivacyPolicy(View):
    def get(self, request):
        context = {}
        return render(request, "privacyPolicy.html", context)

def error_404_view(request, exception):
    return render(request, '404.html')
