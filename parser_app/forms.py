from django import forms
from . import models, film_ru


class ParserCartoonForm(forms.Form):
    MEDIA_CHOICES = (
        ('film.ru', 'film.ru'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = [
            'media_type',
        ]

    def parser_data(self):
        if self.data['media_type'] == 'films.ru':
            disney_parser = film_ru.parser()
            for i in disney_parser:
                models.DisneyCartoon.objects.create(**i)

