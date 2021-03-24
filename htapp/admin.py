from django.contrib import admin
from django.db import models
from htapp.models import (Language, Currency, Country, Hobby, Feature, Special, Facility,
                          HotelCategory, HotelType, Hotel, HotelHobby, HotelPhoto, 
                          HotelFeature, HotelReview, UserInfo, MainSlideBanner)
from django.utils.translation import gettext as _


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'iso_code', 'locale']
    fields = ['name', 'iso_code', 'locale']


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['name', 'iso_code', 'symbol']
    fields = ['name', 'iso_code', 'symbol']


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'iso_code']
    fields = ['name', 'iso_code']
    search_fields = ['name']


@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'is_active']
    fields = ['name', 'name_genitive', 'hobbyist',
              'hobbyist_genitive', 'icon', 'slug', 'is_active']
    search_fields = ['name']


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ['name', 'hobby', 'icon', 'order']
    fields = ['name', 'hobby', 'icon', 'order']
    search_fields = ['name']
    list_filter = ['hobby']


@admin.register(Special)
class SpecialAdmin(admin.ModelAdmin):
    list_display = ['name', 'hobby', 'image', 'icon', 'order']
    fields = ['name', 'hobby', 'image', 'icon', 'order']
    search_fields = ['name']


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon']
    fields = ['name', 'icon']
    search_fields = ['name']


@admin.register(HotelCategory)
class HotelCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon']
    fields = ['name', 'icon']
    search_fields = ['name']


@admin.register(HotelType)
class HotelTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    fields = ['name']
    search_fields = ['name']


class HotelHobbyInline(admin.StackedInline):
    model = HotelHobby
    extra = 0
    fields = ['hobby', 'review', 'reviewer', 'rating']
    readonly_fields = ['rating']


class HotelFeatureInline(admin.TabularInline):
    model = HotelFeature
    extra = 0
    fields = ['feature', 'description']


class HotelPhotoInline(admin.TabularInline):
    model = HotelPhoto
    extra = 0
    fields = ['image']


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['is_active', 'is_promotion', 'category', 'country']
    list_display = ['name', 'category',
                    'country', 'is_active', 'is_promotion', ]
    fieldsets = [
        (None, {'fields': ['name', 'category',
                           'price', 'booking_link', 
                           ('is_active', 'is_promotion'), 'description']}),
        (_('Location'), {'fields': ['country', 'address', 'coordinates']}),
        (_('Attributes'), {'fields': ['types', 'facilities', 'specials']}),
        (_('Photo'), {'fields': ['main_photo']}),
    ]
    filter_horizontal = ['types', 'facilities', 'specials']
    inlines = [HotelPhotoInline, HotelHobbyInline, HotelFeatureInline]
    save_on_top = True


@admin.register(HotelReview)
class HotelReviewAdmin(admin.ModelAdmin):
    list_display = ['hotel', 'hobby', 'reviewer_name',
                    'reviewer_country', 'text_preview', 'rate']
    fields = ['hotel', 'hobby', 'reviewer_name',
              'reviewer_country', 'text', 'rate']


@admin.register(MainSlideBanner)
class MainSlideBannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'order', 'is_active']
    fields = ['title', 'text', 'image', 'order', 'is_active']


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'hobby', 'language', 'currency']
    fields = ['user', 'post', 'hobby', 'language', 'currency']
