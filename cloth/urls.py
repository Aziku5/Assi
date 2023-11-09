from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.ProductView.as_view()),
    path('product_unisex/', views.ProductUnisexView.as_view()),
    path('product_child/', views.ProductChildView.as_view()),
    path('product_woman/', views.ProductWomanView.as_view()),
    path('product_man/', views.ProductManView.as_view()),
    path('cloth_order/', views.OrderFormView.as_view()),
]
