from django.shortcuts import get_object_or_404
from django.views.generic import View, TemplateView
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils.translation import gettext as _
from django.db.models import Count, Max, Min

from .models import Hobby, Hotel, HotelHobby, MainSlideBanner, Country, UserInfo, Special, Facility, HotelCategory, HotelType
from .forms import LoginForm, RegistrationForm
from .templatetags.htapp_extras import pluralize_number


class IndexView(TemplateView):
    '''Главная страница'''

    template_name = 'htapp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        slides = MainSlideBanner.objects.filter(
            is_active=True
        ).order_by('order').values(
            'title', 'text', 'image'
        )
        hotels = Hotel.objects.filter(
            is_active=True, is_promotion=True
        ).order_by('-pk')[:4]
        hobbies = Hobby.objects.filter(is_active=True).order_by('name')
        countries = Country.objects.all().order_by('name')

        context |= {
            'slides': slides,
            'hotels': hotels,
            'hobbies': hobbies,
            'countries': countries,
        }

        return context


class SearchView(TemplateView):
    '''Страница поиска отелей'''

    template_name = 'htapp/search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        hobby = get_object_or_404(Hobby, slug=kwargs['hobby'])
        country = get_object_or_404(Country, pk=kwargs['country'])
        specials = Special.objects.filter(hobby=hobby).order_by('order')
        facilities = Facility.objects.all().order_by('name')
        hotel_types = HotelType.objects.all().order_by('name')
        hotel_categories = HotelCategory.objects.all().order_by('-pk')
        hotels_aggr = Hotel.objects.filter(country=country).aggregate(
            min_price=Min('price'), max_price=Max('price'), count=Count('pk')
        )

        context |= {
            'hobby': hobby,
            'country': country,
            'specials': specials,
            'facilities': facilities,
            'hotel_types': hotel_types,
            'hotel_categories': hotel_categories,
            'hotels_aggr': hotels_aggr,
        }

        return context


class SearchResultsView(TemplateView):
    '''Результаты поиска отелей'''

    template_name = 'htapp/search_results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        selected_specials = self.request.GET.getlist('specials[]', [])
        selected_facilities = self.request.GET.getlist('facilities[]', [])
        selected_hotel_types = self.request.GET.getlist('hotel_types[]', [])
        selected_hotel_categories = self.request.GET.getlist(
            'hotel_categories[]', [])
        price_from = self.request.GET.get('pricefrom', 0)
        price_to = self.request.GET.get('priceto', 0)

        try:
            hobby = Hobby.objects.get(slug=kwargs['hobby'])
            country = Country.objects.get(pk=self.request.GET['country'])
            hotels = Hotel.objects.filter(country=country)

            for selected_special in selected_specials:
                hotels = hotels.filter(specials=selected_special)

            for selected_facility in selected_facilities:
                hotels = hotels.filter(facilities=selected_facility)

            if selected_hotel_types:
                hotels = hotels.filter(types__in=selected_hotel_types)

            if selected_hotel_categories:
                hotels = hotels.filter(category__in=selected_hotel_categories)

            if price_from:
                hotels = hotels.filter(price__gte=price_from)

            if price_to:
                hotels = hotels.filter(price__lte=price_to)

            context |= {
                'hobby': hobby,
                'country': country,
                'hotels': hotels,
                'results_data': {
                    'count': pluralize_number(hotels.count(), 'отель,отеля,отелей')
                }
            }
        except:
            pass

        return context


class HotelView(TemplateView):
    '''Страница отеля'''

    template_name = 'htapp/hotel.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        hobby = get_object_or_404(Hobby, slug=kwargs['hobby'])
        hotel = get_object_or_404(Hotel, pk=kwargs['pk'])
        hotel_hobby = get_object_or_404(
            HotelHobby, hotel=hotel.pk, hobby=hobby.pk)
        photos = hotel.photos.all()
        reviews = hotel.reviews.filter(hobby=hobby).order_by('-pk')
        specials = hotel.specials.filter(hobby=hobby).order_by('order')

        context |= {
            'hobby': hobby,
            'hotel': hotel,
            'hotel_hobby': hotel_hobby,
            'photos': photos,
            'reviews': reviews,
            'specials': specials,
        }

        return context


class LoginView(View):
    '''Авторизация пользователя'''

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return JsonResponse({'ok': True})

        return JsonResponse({'ok': False, 'message': _('User is not found')})


class LogoutView(View):
    '''Выход из учетной записи'''

    def get(self, request):
        logout(request)

        return JsonResponse({'ok': True})


class RegistrationView(View):
    '''Регистрация пользователя'''

    def post(self, request):
        form = RegistrationForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            password = form.cleaned_data['password']
            password_conf = form.cleaned_data['password_conf']

            if password != password_conf:
                return JsonResponse({'ok': False, 'message': _('The passwords do not match')})

            if User.objects.filter(username=email).count() > 0:
                return JsonResponse({'ok': False, 'message': _('Email already registered')})

            user = User.objects.create_user(
                email, email, password, first_name=firstname, last_name=lastname)
            UserInfo.objects.create(user=user)
            login(request, user)

            return JsonResponse({'ok': True})
