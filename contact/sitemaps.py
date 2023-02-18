from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class StaticContactViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.4

    def items(self):
        return ['contact:contact', 'contact:about']

    def location(self, item):
        return reverse(item)