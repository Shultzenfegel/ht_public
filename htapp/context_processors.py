from .models import Currency, Language
from .forms import LoginForm, RegistrationForm


def languages(request):
    '''Добавляет список доступных языков в контекст'''
    return {
        'languages': Language.objects.all()
    }


def currencies(request):
    '''Добавляет список доступных валют в контекст'''
    return {
        'currencies': Currency.objects.all()
    }


def user_forms(request):
    '''Добавляет формы авторизации и регистрации в контекст'''
    return {
        'login_form': LoginForm(),
        'registration_form': RegistrationForm()
    }
