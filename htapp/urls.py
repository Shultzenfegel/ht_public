from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('user/login', views.LoginView.as_view(), name='login'),
    path('user/logout', views.LogoutView.as_view(), name='logout'),
    path('user/registration', views.RegistrationView.as_view(), name='registration'),
    path('<slug:hobby>/search/<int:country>', views.SearchView.as_view(), name='search'),
    path('<slug:hobby>/search-results', views.SearchResultsView.as_view(), name='search-results'),
    path('<slug:hobby>/hotel/<int:pk>', views.HotelView.as_view(), name='hotel'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

