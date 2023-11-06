from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from . import models, film_ru, forms


class ParserCartoonListView(generic.ListView):
    model = models.DisneyCartoon
    template_name = 'film_ru/cartoon_parser_list.html'

    def get_queryset(self):
        return models.DisneyCartoon.objects.all()


class ParserFormView(generic.FormView):
    template_name = 'film_ru/start_pars.html'
    form_class = forms.ParserCartoonForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('Данные успешно взяты....')
        else:
            return super(ParserFormView, self).post(request, *args, **kwargs)
