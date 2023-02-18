from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class StaticPricingViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        return ['pricing:pricing']

    def location(self, item):
        return reverse(item)