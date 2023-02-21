from django.shortcuts import render
from django.views import View

class Home(View):
    def get(self, request):
        context = {}
        return render(request, "home.html", context)

def error_404_view(request, exception):
    return render(request, '404.html')
