from django.urls import path
from . import views

urlpatterns = [
    path('cartoon_list_parser/', views.ParserCartoonListView.as_view()),
    path('start_pars/', views.ParserFormView.as_view()),
]
