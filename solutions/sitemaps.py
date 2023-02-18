from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class StaticSolutionsViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 1.0

    def items(self):
        return ['solutions:website', 'solutions:mobileApp']

    def location(self, item):
        return reverse(item)