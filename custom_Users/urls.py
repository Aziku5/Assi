from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('registrations/', views.RegistrationView.as_view()),
    path('login/', views.AuthLoginView.as_view(), name='home'),
    path('logout/', views.AuthLogoutView.as_view(), name='logout'),
    path('homepage/', views.UserListView.as_view(), name='post'),
]

