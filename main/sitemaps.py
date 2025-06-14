from django.contrib.sitemaps import Sitemap
from .models import Destination, News
from django.urls import reverse


class DestinationSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Destination.objects.all()

    def lastmod(self, obj):
        return obj.created_at  # или updated_at если есть

    def location(self, obj):
        return obj.get_absolute_url()


class NewsSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return News.objects.all()

    def lastmod(self, obj):
        return obj.created_at  # или updated_at если есть

    def location(self, obj):
        return obj.get_absolute_url()


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return ['home', 'about-us', 'contact', 'faq', 'trips', 'news', 'reviews']

    def location(self, item):
        return reverse(item)
