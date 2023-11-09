from django.shortcuts import get_object_or_404
from . import models, forms
from django.views.generic import ListView, DetailView
from django.views import generic


class ProductView(ListView):
    queryset = models.ProductCL.objects.filter().order_by('-id')
    template_name = 'clothes/product.html'

    def get_queryset(self):
        return models.ProductCL.objects.filter().order_by('-id')


class ProductUnisexView(ListView):
    queryset = models.ProductCL.objects.filter(tags__name='UnisexCl')
    template_name = 'clothes/product_unisexcl.html'

    def get_queryset(self):
        return models.ProductCL.objects.filter(tags__name='UnisexCl')


class ProductChildView(ListView):
    queryset = models.ProductCL.objects.filter(tags__name='ClidCl')
    template_name = 'clothes/product_childcl.html'

    def get_queryset(self):
        return models.ProductCL.objects.filter(tags__name='ChildCl')


class ProductWomanView(ListView):
    queryset = models.ProductCL.objects.filter(tags__name='WomanCl')
    template_name = 'clothes/product_womancl.html'

    def get_queryset(self):
        return models.ProductCL.objects.filter(tags__name='WomanCl')


class ProductManView(ListView):
    queryset = models.ProductCL.objects.filter(tags__name='ManCl')
    template_name = 'clothes/product_mancl.html'

    def get_queryset(self):
        return models.ProductCL.objects.filter(tags__name='ManCl')


class OrderFormView(generic.CreateView):
    template_name = 'clothes/cloth_order.html'
    form_class = forms.OrderForm
    queryset = models.OrderCL.objects.all()
    success_url = '/product/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(OrderFormView, self).form_valid(form=form)