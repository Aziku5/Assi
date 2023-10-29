from django.urls import path
from . import views

urlpatterns = [
    path('all_cartoons/', views.CartoonListView.as_view(), name='allCartoons'),
    path('cartoon_detail/<int:id>/', views.CartoonDetailView.as_view(), name='detail'),
    path('cartoon_detail/<int:id>/delete/', views.DeleteCartoonView.as_view(), name='delete'),
    path('cartoon_detail/<int:id>/update/', views.UpdateCartoonView.as_view(), name='update'),
    path('create_cartoon/', views.CreateCartoonView.as_view(), name='createCartoon'),
    path('search/', views.Search.as_view(), name='search'),
]
