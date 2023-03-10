"""aliyo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap

from home.sitemaps import StaticHomeViewSitemap
from contact.sitemaps import StaticContactViewSitemap
from pricing.sitemaps import StaticPricingViewSitemap
from solutions.sitemaps import StaticSolutionsViewSitemap

sitemaps = {
    'staticHome' : StaticHomeViewSitemap,
    'staticSolutions' : StaticSolutionsViewSitemap,
    'staticContact' : StaticContactViewSitemap,
    'staticPricing' : StaticPricingViewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('home.urls', 'home'))),
    path('', include(('contact.urls', 'home'))),
    path('', include(('solutions.urls', 'home'))),
    path('', include(('pricing.urls', 'home'))),
    path('sitemap.xml', sitemap, {'sitemaps' : sitemaps}),
]

handler404 = 'home.views.error_404_view'
