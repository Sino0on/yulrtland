from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'mini_description', 'description')


@register(Features)
class FeaturesTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Destination)
class FeaturesTranslationOptions(TranslationOptions):
    fields = ('title', 'type', 'mini_title', 'description', 'accomodation', 'transportation', 'map')


@register(Itenary)
class FeaturesTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(DatePrice)
class FeaturesTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Review)
class FeaturesTranslationOptions(TranslationOptions):
    fields = ('country', 'content')


@register(BlockInfo)
class FeaturesTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Tag)
class FeaturesTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Category)
class FeaturesTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Faq)
class FeaturesTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')


@register(Quiz)
class FeaturesTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Question)
class FeaturesTranslationOptions(TranslationOptions):
    fields = ('text',)


@register(AnswerOption)
class FeaturesTranslationOptions(TranslationOptions):
    fields = ('text',)


@register(FaqCategory)
class FeaturesTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
