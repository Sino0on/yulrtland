from django.urls import path
from .views import *
from django.conf.urls import handler404


handler404 = 'main.views.custom_404'


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('trips/<int:pk>', trip_detail, name='trip_detail'),
    path('trips', TripListView.as_view(), name='trips'),
    path('about-us', AboutUsView.as_view(), name='about-us'),
    path('news', NewsListView.as_view(), name='news'),
    path('news/<int:pk>', NewsDetailView.as_view(), name='news_detail'),
    path('reviews', ReviewsView.as_view(), name='reviews'),
    path('faq', FAQView.as_view(), name='faq'),
    path('contact', contact_view, name='contact'),
    path('<int:quiz_id>/start/', quiz_start, name='quiz_start'),
    path('question/<int:question_id>/', quiz_question, name='quiz_question'),
    path('<int:quiz_id>/submit/', quiz_submit, name='quiz_submit'),
    path('subscribe/', subscribe_newsletter, name='subscribe_newsletter'),
    path('icons/', icons, name='icons'),

]
