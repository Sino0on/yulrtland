from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('trips/<int:pk>', trip_detail, name='trip_detail'),
    path('trips', TripListView.as_view(), name='trips'),
    path('about-us', AboutUsView.as_view(), name='about-us'),
    path('news', NewsListView.as_view(), name='news'),
    path('news/<int:pk>', NewsDetailView.as_view(), name='news_detail'),
]
