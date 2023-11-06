from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

MALE = 1
FEMALE = 2

GENDER_TYPE = (
    (MALE, 'Мужчина'),
    (FEMALE, 'Женщина')
)

MARRIED = 1
FREE = 2

MARRY = (
    (MARRIED, 'Да'),
    (FREE, 'Нет')
)

YES = 1
NO = 2

ANIMAL = (
    (YES, 'Да'),
    (NO, 'Нет')
)


class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True, initial='+996', label='Укажите ваш номер')
    date_birth = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=GENDER_TYPE, required=True)
    age = forms.IntegerField(required=True, verbose_name='Введите возраст')
    hobby = forms.CharField(max_length=99, verbose_name='Ваше хобби')
    job = forms.CharField(max_length=50, verbose_name='Место работы/учебы')
    married = forms.IntegerField(choices=MARRY, verbose_name='Женаты/замужем ли вы?')
    height = forms.CharField(max_length=5, verbose_name='Сколько вы весите?')
    animal = forms.CharField(choices=ANIMAL, verbose_name='У вас есть домашнее животное?')
    name_animal = forms.CharField(max_length=50, verbose_name='Укажите имя вашего питомца')

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'phone_number',
            'date_birth',
            'gender',
            'age',
            'hobby',
            'job',
            'married',
            'animal',
            'height',
            'name_animal',
        )

    def save(self, commit=True):
        user = super(CustomRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
