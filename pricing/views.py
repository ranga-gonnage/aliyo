from django.shortcuts import render
from django.views import View

class Pricing(View):
    def get(self, request):
        context = {}
        return render(request, "pricing.html", context)