from email.message import EmailMessage

from django.contrib import admin
from .models import *

class ImagesInline(admin.StackedInline):
    model = ImageGalleryDestination
    extra = 1

class ItenaryInline(admin.StackedInline):
    model = Itenary
    extra = 1

@admin.register(Destination)
class Section6Admin(admin.ModelAdmin):
    inlines = [
        ImagesInline,
        ItenaryInline
    ]
    filter_horizontal = ('features',)

admin.site.register(ImageGalleryDestination)
admin.site.register(Itenary)
admin.site.register(Features)
admin.site.register(BlockInfo)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(News)
admin.site.register(SiteSetting)
admin.site.register(Review)
admin.site.register(Faq)

from django.contrib import admin
from .models import Quiz, Question, AnswerOption, QuizSubmission, SubmissionAnswer

class AnswerOptionInline(admin.TabularInline):
    model = AnswerOption
    extra = 2

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1
    inlines = [AnswerOptionInline]

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerOptionInline]
    list_display = ['text', 'quiz', 'order']
    list_filter = ['quiz']
    ordering = ['quiz', 'order']

class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ['title', 'is_active']
    list_filter = ['is_active']

class SubmissionAnswerInline(admin.TabularInline):
    model = SubmissionAnswer
    extra = 0
    readonly_fields = ['question', 'selected_option']

class QuizSubmissionAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'contact', 'quiz', 'submitted_at']
    list_filter = ['quiz', 'submitted_at']
    readonly_fields = ['submitted_at']
    inlines = [SubmissionAnswerInline]

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(QuizSubmission, QuizSubmissionAdmin)
admin.site.register(TripBooking)
admin.site.register(NewsletterSubscriber)
admin.site.register(ContactMessage)
admin.site.register(FaqCategory)



# @admin.register(News)
# class NewsAdmin(admin.ModelAdmin):
#
#     # filter_horizontal = ('Tags',)


