from django.urls import path
from . import views

urlpatterns = [
    path('all_cartoons/', views.cartoonView, name='allCartoons'),
    path('cartoon_detail/<int:id>/', views.cartoonDetailView, name='detail')
]