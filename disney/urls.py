from django.urls import path
from . import views

urlpatterns = [
    path('all_cartoons/', views.cartoonView, name='allCartoons'),
    path('cartoon_detail/<int:id>/', views.cartoonDetailView, name='detail'),
    path('cartoon_detail/<int:id>/delete/', views.deleteCartoonView, name='delete'),
    path('cartoon_detail/<int:id>/update/', views.updateCartoonView, name='update'),
    path('create_cartoon/', views.creatCartoonView, name='createCartoon'),
]
