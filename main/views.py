from pyexpat import features

from django.shortcuts import render
from django.views import generic

from .filters import DestinationFilter
from .models import *
from decouple import config


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
        context['infoblocks'] = BlockInfo.objects.all()
        return context



# def trip_detail(request, pk):
#     destination = Destination.objects.get(pk=pk)
#     cimular_trips = Destination.objects.all()[:3]
#     return render(request, 'trip_detail.html', {'trip': destination, 'cimular_trips': cimular_trips, 'best_tours': Destination.objects.all()[:5]})


def trip_detail(request, slug):
    trip = get_object_or_404(Destination, slug=slug)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')
        number_person = request.POST.get('number_person')

        booking = TripBooking.objects.create(
            trip=trip,
            name=name,
            email=email,
            phone=phone,
            from_date=from_date,
            to_date=to_date,
            number_person=number_person
        )
        message = (
            f"📩 New Trip Booking!\n"
            f"👤 *Name:* {booking.name}\n"
            f"📧 *Email:* {booking.email}\n"
            f"📞 *Phone:* {booking.phone}\n"
            f"🗓 *Dates:* {booking.from_date} → {booking.to_date}\n"
            f"👥 *People:* {booking.number_person}\n"
            f"🌄 *Trip:* {booking.trip.title}"
        )
        send_telegram_notification(message, booking.id, "main/tripbooking")
        messages.success(request, 'Thank you! Your booking has been received.')
        return redirect('trip_detail', pk=trip.pk)
    cimular_trips = Destination.objects.all()[:3]

    included = trip.features.all()
    not_included = Features.objects.exclude(id__in=included.values_list('id', flat=True))

    return render(request, 'trip_detail.html', {'trip': trip, 'cimular_trips': cimular_trips, 'best_tours': Destination.objects.all()[:5], 'included': included, "not_included": not_included})



class TripListView(generic.ListView):
    model = Destination
    context_object_name = 'trips'
    queryset = Destination.objects.all()
    template_name = 'trips.html'
    filterset_class = DestinationFilter
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = SiteSetting.objects.all().first()
        context['categories'] = Category.objects.all()
        context['best_tours'] = Destination.objects.all()[:5]
        context['levels'] = ['easy', 'medium', 'difficult', 'hard', 'extreme']
        context['numbers'] = [1, 2, 3, 4, 5]
        return context


class AboutUsView(generic.TemplateView):
    template_name = 'about_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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
        context['last_news'] = News.objects.all()[:3]
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


class ReviewsView(generic.TemplateView):
    template_name = 'reviews.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = SiteSetting.objects.all().first()
        context['destinations'] = Destination.objects.all()[:4]
        context['best_tours'] = Destination.objects.all()[:5]
        context['reviews'] = Review.objects.all()
        return context


class FAQView(generic.TemplateView):
    template_name = 'faq.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = SiteSetting.objects.all().first()
        context['destinations'] = Destination.objects.all()[:4]
        context['best_tours'] = Destination.objects.all()[:5]
        context['reviews'] = Review.objects.all()
        # context['faq'] = Faq.objects.all()
        context['categories'] = FaqCategory.objects.all()
        return context


class ContactUsView(generic.TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = SiteSetting.objects.all().first()
        context['destinations'] = Destination.objects.all()[:4]
        context['best_tours'] = Destination.objects.all()[:5]
        context['reviews'] = Review.objects.all()
        return context


from django.shortcuts import render, get_object_or_404, redirect
from .models import Quiz, Question, AnswerOption, QuizSubmission, SubmissionAnswer

def quiz_start(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id, is_active=True)
    first_question = quiz.questions.order_by('order').first()
    if not first_question:
        return render(request, 'quiz/empty.html', {'quiz': quiz})
    return redirect('quiz_question', question_id=first_question.id)

def quiz_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    quiz = question.quiz
    all_questions = quiz.questions.order_by('order')
    current_index = list(all_questions).index(question)
    is_last = current_index == len(all_questions) - 1

    if request.method == 'POST':
        selected_options = request.POST.getlist('answers')
        if 'quiz_answers' not in request.session:
            request.session['quiz_answers'] = {}
        request.session['quiz_answers'][str(question.id)] = selected_options
        request.session.modified = True

        if not is_last:
            next_question = all_questions[current_index + 1]
            return redirect('quiz_question', question_id=next_question.id)
        else:
            return redirect('quiz_submit', quiz_id=quiz.id)

    return render(request, 'quiz/question.html', {
        'quiz': quiz,
        'question': question,
        'options': question.options.all(),
        'is_last': is_last,
    })

def quiz_submit(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        contact = request.POST.get('contact')
        answers = request.session.get('quiz_answers', {})

        submission = QuizSubmission.objects.create(
            full_name=full_name,
            contact=contact,
            quiz=quiz
        )

        for question_id_str, selected_option_ids in answers.items():
            question = Question.objects.get(id=int(question_id_str))
            for option_id in selected_option_ids:
                option = AnswerOption.objects.get(id=int(option_id))
                SubmissionAnswer.objects.create(
                    submission=submission,
                    question=question,
                    selected_option=option
                )

        # Clean up
        request.session.pop('quiz_answers', None)
        message = (
            f"🧠 *New Quiz Submission*\n"
            f"👤 *Name:* {submission.full_name}\n"
            f"📞 *Contact:* {submission.contact}\n"
            f"📋 *Quiz:* {submission.quiz.title}"
        )
        send_telegram_notification(message, submission.id, "main/quizsubmission")

        return render(request, 'quiz/thank_you.html', {'full_name': full_name})

    return render(request, 'quiz/submit.html', {'quiz': quiz})


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage

def contact_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact = ContactMessage.objects.create(
            full_name=full_name,
            email=email,
            message=message
        )
        message = (
            f"📬 *New Contact Message*\n"
            f"👤 *Name:* {contact.full_name}\n"
            f"📧 *Email:* {contact.email}\n"
            f"💬 *Message:* {contact.message}"
        )
        send_telegram_notification(message, contact.id, "main/contactmessage")
        messages.success(request, 'Thank you! Your message has been sent.')
        return redirect('contact')

    return render(request, 'contact.html', {"about": SiteSetting.objects.all().first()})


import requests
from django.urls import reverse

import requests

def send_telegram_notification(text, booking_id=None, model_admin_path=None):
    bot_token = config('BOT_TOKEN')
    chat_id = "-1002572536402"

    if booking_id and model_admin_path:
        admin_url = f"https://yurthorizon.com/admin/{model_admin_path}/{booking_id}/change/"
        text += f"\n\n🔗 [View in Admin Panel]({admin_url})"

    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown"
    }

    try:
        requests.post(f"https://api.telegram.org/bot{bot_token}/sendMessage", data=payload, timeout=5)
    except Exception as e:
        print("Telegram error:", e)



def subscribe_newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        if email:
            _, created = NewsletterSubscriber.objects.get_or_create(email=email)
            if created:
                messages.success(request, "Thanks for subscribing!")
            else:
                messages.info(request, "You're already subscribed.")

    return redirect(request.META.get('HTTP_REFERER', '/'))


def custom_404(request, exception):
    return render(request, '404_page.html', status=404)


def icons(request):
    return render(request, 'iconfont.html', status=404)
