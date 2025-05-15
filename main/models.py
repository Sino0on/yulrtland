from django.db import models
from ckeditor.fields import RichTextField

ranks = (
    ('Easy', 'Easy'),
    ('Medium', 'Medium'),
    ('Hard', 'Hard'),
    ('Extreme', 'Extreme'),
)

class Features(models.Model):
    title = models.CharField(max_length=123)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['-created_at']


class Destination(models.Model):
    title = models.CharField(max_length=255)
    oblasti = models.CharField(max_length=255)
    days = models.CharField(max_length=255)
    nights = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    level = models.CharField(max_length=123, choices=ranks)
    max_height = models.CharField(max_length=123, blank=True, null=True)
    type = models.CharField(max_length=123, blank=True, null=True)
    trip_days = models.CharField(max_length=123, blank=True, null=True)
    start = models.CharField(max_length=123, blank=True, null=True)
    mini_title = models.CharField(max_length=123, blank=True, null=True)
    description = RichTextField()
    code = models.CharField(max_length=123, blank=True, null=True)
    accomodation = models.CharField(max_length=123, blank=True, null=True)

    transportation = models.CharField(max_length=123, blank=True, null=True)

    image = models.FileField(upload_to='destinations/')
    map = models.FileField(upload_to='maps/', blank=True, null=True)
    features = models.ManyToManyField(Features)
    created_at = models.DateTimeField()

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['-created_at']


class Itenary(models.Model):
    title = models.CharField(max_length=123, blank=True, null=True)
    day = models.CharField(max_length=123, blank=True, null=True)
    destination = models.ForeignKey(Destination, on_delete=models.SET_NULL, related_name='iternaries', null=True, blank=True)
    icon = models.CharField(max_length=123, blank=True, null=True)
    created_at = models.DateTimeField()

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['-created_at']


class DatePrice(models.Model):
    title = models.CharField(max_length=123, blank=True, null=True)
    status = models.BooleanField(default=True)
    discount = models.CharField(max_length=123, blank=True, null=True)
    price = models.CharField(max_length=123, blank=True, null=True)
    destination = models.ForeignKey(Destination, on_delete=models.SET_NULL, related_name='prices', null=True,
                                    blank=True)
    created_at = models.DateTimeField()

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['-created_at']


class Review(models.Model):
    full_name = models.CharField(max_length=123, blank=True, null=True)
    reiting = models.CharField(max_length=1, blank=True, null=True)
    country = models.CharField(max_length=123, blank=True, null=True)
    image = models.ImageField(upload_to='avatars/')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.full_name}'

    class Meta:
        ordering = ['-created_at']


class ImageGalleryDestination(models.Model):
    image = models.FileField(upload_to='gallery/')
    status = models.BooleanField(default=True)
    destination = models.ForeignKey(Destination, on_delete=models.SET_NULL, related_name='images', null=True,
                                    blank=True)
    created_at = models.DateTimeField()

    def __str__(self):
        return f'{self.pk} - {self.destination}'

    class Meta:
        ordering = ['-created_at']


class BlockInfo(models.Model):
    title = models.CharField(max_length=123)
    description = models.TextField()
    icon = models.CharField(max_length=123)
    created_at = models.DateTimeField()

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['-created_at']


class Tag(models.Model):
    title = models.CharField(max_length=123)
    created_at = models.DateTimeField()

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=123)
    created_at = models.DateTimeField()

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['-created_at']



class News(models.Model):
    title = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    mini_description = models.CharField(max_length=255)
    description = RichTextField()
    author = models.CharField(max_length=123)
    created_at = models.DateTimeField()
    image = models.FileField(upload_to='images/')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['-created_at']



class SingletonModel(models.Model):
    """
    Модель, которая всегда имеет только один экземпляр.
    """

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        # Если модель уже существует, удалите ее
        self.__class__.objects.exclude(id=self.id).delete()
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        # Если модель еще не существует, создайте ее
        if not cls.objects.exists():
            cls.objects.create()
        return cls.objects.get()


class SiteSetting(SingletonModel):
    contacts = models.TextField(blank=True, verbose_name='Контакт')
    emails = models.TextField(blank=True, verbose_name='Почта')
    title = models.CharField(max_length=123, blank=True, null=True, verbose_name='Название компании')
    photo_video = models.ImageField(upload_to='images', blank=True, null=True, verbose_name='Название компании')
    description = RichTextField(blank=True, null=True, verbose_name='О нас')
    image_about = models.FileField(upload_to='images')
    image_blog = models.FileField(upload_to='images')
    image_trip = models.FileField(upload_to='images')
    address_map = models.TextField( verbose_name="Адрес на карте", default='''
    <a class="dg-widget-link" href="http://2gis.kg/bishkek/firm/70000001021088130/center/74.587426,42.845011/zoom/16?utm_medium=widget-source&utm_campaign=firmsonmap&utm_source=bigMap">Посмотреть на карте Бишкека</a><div class="dg-widget-link"><a href="http://2gis.kg/bishkek/firm/70000001021088130/photos/70000001021088130/center/74.587426,42.845011/zoom/17?utm_medium=widget-source&utm_campaign=firmsonmap&utm_source=photos">Фотографии компании</a></div><div class="dg-widget-link"><a href="http://2gis.kg/bishkek/center/74.587426,42.845011/zoom/16/routeTab/rsType/bus/to/74.587426,42.845011╎Кыргызский Государственный Технический Университет им. И. Раззакова, ректорат?utm_medium=widget-source&utm_campaign=firmsonmap&utm_source=route">Найти проезд до Кыргызский Государственный Технический Университет им. И. Раззакова, ректорат</a></div><script charset="utf-8" src="https://widgets.2gis.com/js/DGWidgetLoader.js"></script><script charset="utf-8">new DGWidgetLoader({"width":640,"height":600,"borderColor":"#a3a3a3","pos":{"lat":42.845011,"lon":74.587426,"zoom":16},"opt":{"city":"bishkek"},"org":[{"id":"70000001021088130"}]});</script><noscript style="color:#c00;font-size:16px;font-weight:bold;">Виджет карты использует JavaScript. Включите его в настройках вашего браузера.</noscript>
    ''')

    class Meta:
        verbose_name = 'Настройка сайта'
        verbose_name_plural = 'Настройки сайта'


