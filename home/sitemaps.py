from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class StaticHomeViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return ['home:home', 'home:legalNotice', 'home:privacyPolicy']

    def location(self, item):
        return reverse(item)