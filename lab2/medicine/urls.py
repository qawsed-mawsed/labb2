# medicine/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('main/', views.main, name='main'),
    # Добавь другие URL-маршруты, если необходимо
]
