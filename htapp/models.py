from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext as _


class Language(models.Model):
    '''Язык'''
    name = models.CharField(_('Name'), max_length=50)
    iso_code = models.CharField(_('ISO Code'), max_length=2, default='')
    locale = models.CharField(_('Locale'), max_length=50, default='')

    class Meta:
        verbose_name = _('Language')
        verbose_name_plural = _('Languages')

    def __str__(self):
        return self.name


class Currency(models.Model):
    '''Валюта'''
    name = models.CharField(_('Name'), max_length=50)
    iso_code = models.CharField(_('ISO Code'), max_length=3, default='')
    symbol = models.CharField(_('Symbol'), max_length=1, default='')

    class Meta:
        verbose_name = _('Currency')
        verbose_name_plural = _('Currencies')

    def __str__(self):
        return self.name


class Country(models.Model):
    '''Страна'''
    name = models.CharField(_('Name'), max_length=250)
    iso_code = models.CharField(
        _('ISO Code'), max_length=2, default='', blank=True)

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')

    def __str__(self):
        return self.name


class Hobby(models.Model):
    '''Хобби'''
    name = models.CharField(_('Name'), max_length=250)
    name_genitive = models.CharField(_('Name (genitive)'), max_length=250)
    hobbyist = models.CharField(_('Hobbyist name'), max_length=250)
    hobbyist_genitive = models.CharField(
        _('Hobbyist name (genitive)'), max_length=250)
    icon = models.FileField(_('Icon'), upload_to='hobby/', blank=True)
    slug = models.SlugField(_('Slug'), default='')
    is_active = models.BooleanField(_('Is active'), default=True)

    class Meta:
        verbose_name = _('Hobby')
        verbose_name_plural = _('Hobbies')

    def __str__(self):
        return self.name


class Feature(models.Model):
    '''Особенность'''
    name = models.CharField(_('Name'), max_length=250)
    hobby = models.ForeignKey(Hobby, verbose_name=_(
        'Hobby'), on_delete=models.CASCADE)
    icon = models.FileField(_('Icon'), upload_to='feature/', blank=True)
    order = models.IntegerField(_('Order'), default=0)

    class Meta:
        verbose_name = _('Feature')
        verbose_name_plural = _('Features')

    def __str__(self):
        return self.name


class Special(models.Model):
    '''Специальная услуга'''
    name = models.CharField(_('Name'), max_length=250)
    hobby = models.ForeignKey(Hobby, verbose_name=_(
        'Hobby'), on_delete=models.CASCADE)
    image = models.ImageField(_('Image'), upload_to='special/', blank=True)
    icon = models.FileField(_('Icon'), upload_to='special/', blank=True)
    order = models.IntegerField(_('Order'), default=0)

    class Meta:
        verbose_name = _('Special')
        verbose_name_plural = _('Specials')

    def __str__(self):
        return self.name


class Facility(models.Model):
    '''Удобство'''
    name = models.CharField(_('Name'), max_length=250)
    icon = models.FileField(_('Icon'), upload_to='facility/', blank=True)

    class Meta:
        verbose_name = _('Facility')
        verbose_name_plural = _('Facilities')

    def __str__(self):
        return self.name


class HotelCategory(models.Model):
    '''Категория отеля'''
    name = models.CharField(_('Name'), max_length=250)
    icon = models.FileField(_('Icon'), upload_to='hotelcategory/', blank=True)

    class Meta:
        verbose_name = _('Hotel category')
        verbose_name_plural = _('Hotel categories')

    def __str__(self):
        return self.name


class HotelType(models.Model):
    '''Тип отеля'''
    name = models.CharField(_('Name'), max_length=250)

    class Meta:
        verbose_name = _('Hotel type')
        verbose_name_plural = _('Hotel types')

    def __str__(self):
        return self.name


class Hotel(models.Model):
    '''Отель'''
    name = models.CharField(_('Name'), max_length=250)
    category = models.ForeignKey(
        HotelCategory, verbose_name=_('Category'), on_delete=models.PROTECT)
    country = models.ForeignKey(
        Country, verbose_name=_('Country'), on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(
        _('Address'), max_length=500, default='', blank=True)
    #lon = models.FloatField(_('Longitude'), default=0, blank=True)
    #lat = models.FloatField(_('Latitude'), default=0, blank=True)
    coordinates = models.CharField(
        _('Coordinates'), max_length=50, default='', blank=True)
    types = models.ManyToManyField(
        HotelType, verbose_name=_('Hotel types'), blank=True)
    main_photo = models.ImageField(
        _('Main photo'), upload_to='hotel/', blank=True)
    description = models.TextField(_('Description'), default='', blank=True)
    price = models.DecimalField(
        _('Price'), max_digits=20, decimal_places=2, default=0)
    is_active = models.BooleanField(_('Is active'), default=True)
    is_promotion = models.BooleanField(_('Is promotion'), default=True)
    facilities = models.ManyToManyField(
        Facility, verbose_name=_('Facilities'), blank=True)
    specials = models.ManyToManyField(
        Special, verbose_name=_('Specials'), blank=True)
    booking_link = models.URLField(_('Booking link'), default='', blank=True)

    class Meta:
        verbose_name = _('Hotel')
        verbose_name_plural = _('Hotels')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('hotel', kwargs={'pk': self.pk})


class HotelHobby(models.Model):
    '''Хобби в отеле'''
    hotel = models.ForeignKey(Hotel, verbose_name=_(
        'Hotel'), on_delete=models.CASCADE, related_name='hotelhobbies')
    hobby = models.ForeignKey(Hobby, verbose_name=_(
        'Hobby'), on_delete=models.CASCADE, related_name='hotelhobbies')
    review = models.TextField(_('Review'), default='', blank=True)
    reviewer = models.ForeignKey(
        User, verbose_name=_('Reviewer'), on_delete=models.SET_NULL, null=True, blank=True)
    rating = models.DecimalField(
        _('Rating'), max_digits=4, decimal_places=2, default=0)

    class Meta:
        verbose_name = _('Hotel hobby')
        verbose_name_plural = _('Hotel hobbies')
        constraints = [
            models.UniqueConstraint(
                fields=['hotel', 'hobby'], name='uq_hotel_hobby')
        ]

    def __str__(self):
        return f'{self.hotel.name} / {self.hobby.name}'


class HotelPhoto(models.Model):
    '''Фотографии отеля'''
    hotel = models.ForeignKey(
        Hotel, verbose_name=_('Hotel'), on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(_('Image'), upload_to='hotel/', blank=True)

    class Meta:
        verbose_name = _('Hotel photo')
        verbose_name_plural = _('Hotel photos')

    def __str__(self):
        return self.hotel.name


class HotelFeature(models.Model):
    '''Особенность в отеле'''
    hotel = models.ForeignKey(
        Hotel, verbose_name=_('Hotel'), on_delete=models.CASCADE, related_name='hotel_features')
    feature = models.ForeignKey(
        Feature, verbose_name=_('Feature'), on_delete=models.CASCADE)
    description = models.TextField(_('Description'), default='', blank=True)

    class Meta:
        verbose_name = _('Hotel feature')
        verbose_name_plural = _('Hotel features')
        constraints = [
            models.UniqueConstraint(
                fields=['hotel', 'feature'], name='uq_hotel_feature')
        ]

    def __str__(self):
        return f"{self.hotel.name} / {self.feature.name}"


class HotelReview(models.Model):
    '''Отзыв об отеле'''
    hotel = models.ForeignKey(
        Hotel, verbose_name=_('Hotel'), on_delete=models.CASCADE, related_name='reviews')
    hobby = models.ForeignKey(
        Hobby, verbose_name=_('Hobby'), on_delete=models.SET_NULL, null=True, blank=True)
    reviewer_name = models.CharField(
        _('Reviewer name'), max_length=250, default='', blank=True)
    reviewer_country = models.ForeignKey(
        Country, verbose_name=_('Country'), on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField(_('Text'), default='', blank=True)
    rate = models.IntegerField(_('Rate'), default=0)

    class Meta:
        verbose_name = _('Review')
        verbose_name_plural = _('Reviews')

    def __str__(self):
        return self.reviewer_name

    def text_preview(self):
        return self.text[:50] + "..."


class UserInfo(models.Model):
    '''Дополнительная информация о пользователе'''
    user = models.OneToOneField(
        User, verbose_name=_('User'), on_delete=models.CASCADE, related_name='info')
    post = models.CharField(_('Post'), max_length=250, default='', blank=True)
    hobby = models.ForeignKey(
        Hobby, verbose_name=_('Hobby'), on_delete=models.SET_NULL, null=True, blank=True)
    language = models.ForeignKey(
        Language, verbose_name=_('Language'), on_delete=models.SET_NULL, null=True, blank=True)
    currency = models.ForeignKey(
        Currency, verbose_name=_('Currency'), on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = _('User information')
        verbose_name_plural = _('User informations')

    def __str__(self):
        return self.user.username


class MainSlideBanner(models.Model):
    '''Слайд-баннер на главной странице'''
    title = models.CharField(_('Title'), max_length=250)
    text = models.TextField(_('Text'), max_length=500, default='', blank=True)
    image = models.ImageField(_('Image'), upload_to='slider/', blank=True)
    order = models.IntegerField(_('Order'), default=0)
    is_active = models.BooleanField(_('Is active'), default=True)

    class Meta:
        verbose_name = _("Main slide banner")
        verbose_name_plural = _("Main slide banners")

    def __str__(self):
        return self.title
