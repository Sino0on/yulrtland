from django.shortcuts import render
from django.views import generic
from .models import *


# def home(request):
#     destinations = Destination.objects.all()
#     infoblocks = BlockInfo.objects.all()
#     return render(request, 'index.html', {'destinations': destinations, 'infoblocks': infoblocks, 'best_tours': Destination.objects.all()[:5]})

class HomeView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = SiteSetting.objects.all().first()
        context['destinations'] = Destination.objects.all()[:4]
        context['best_tours'] = Destination.objects.all()[:5]
        context['reviews'] = Review.objects.all()
        return context


def trip_detail(request, pk):
    destination = Destination.objects.get(pk=pk)
    cimular_trips = Destination.objects.all()[:3]
    return render(request, 'trip_detail.html', {'trip': destination, 'cimular_trips': cimular_trips, 'best_tours': Destination.objects.all()[:5]})


class TripListView(generic.ListView):
    model = Destination
    context_object_name = 'trips'
    queryset = Destination.objects.all()
    template_name = 'trips.html'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = SiteSetting.objects.all().first()
        context['categories'] = Category.objects.all()
        context['best_tours'] = Destination.objects.all()[:5]
        return context


class AboutUsView(generic.TemplateView):
    template_name = 'about_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = SiteSetting.objects.all().first()
        context['about'] = SiteSetting.objects.all().first()
        context['categories'] = Category.objects.all()
        context['reviews'] = Review.objects.all()
        context['best_tours'] = Destination.objects.all()[:5]
        return context


class NewsListView(generic.ListView):
    template_name = 'blog_list2.html'
    queryset = News.objects.all()
    model = News
    paginate_by = 5
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = SiteSetting.objects.all().first()
        context['best_tours'] = Destination.objects.all()[:5]
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        return context


class NewsDetailView(generic.DetailView):
    template_name = 'blog_single.html'
    queryset = News.objects.all()
    model = News
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['best_tours'] = Destination.objects.all()[:5]
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        print(context)
        return context



