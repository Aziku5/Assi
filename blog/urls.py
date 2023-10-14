from django.urls import path
from . import views

urlpatterns = [
    path('mypost_link/', views.postVew, name='posts')
]