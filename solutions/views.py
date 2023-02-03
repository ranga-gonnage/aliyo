from django.shortcuts import render

class WebSite(View):
    def get(self, request):
        context = {}
        return render(request, "website.html", context)


class MobileApp(View):
    def get(self, request):
        context = {}
        return render(request, "mobileApp.html", context)
