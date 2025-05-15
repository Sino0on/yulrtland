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


# @admin.register(News)
# class NewsAdmin(admin.ModelAdmin):
#
#     # filter_horizontal = ('Tags',)

