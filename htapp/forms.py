from django import forms
from django.utils.translation import gettext as _


class LoginForm(forms.Form):
    '''Форма авторизации'''
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'signInUsername',
                'class': 'b-field__input',
                'placeholder': _('Login/email')
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'id': 'signInPassword',
                'class': 'b-field__input',
                'placeholder': _('Password')
            }
        )
    )


class RegistrationForm(forms.Form):
    '''Форма регистрации'''
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                'id': 'signUpEmail',
                'class': 'b-field__input',
                'placeholder': _('Email')
            }
        )
    )
    firstname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'signUpFirstName',
                'class': 'b-field__input',
                'placeholder': _('First name')
            }
        )
    )
    lastname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'signUpLastName',
                'class': 'b-field__input',
                'placeholder': _('Last name')
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'id': 'signUpPassword',
                'class': 'b-field__input',
                'placeholder': _('Password')
            }
        )
    )
    password_conf = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'id': 'signUpPasswordConf',
                'class': 'b-field__input',
                'placeholder': _('Confirm password')
            }
        )
    )
