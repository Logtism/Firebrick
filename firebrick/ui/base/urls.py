from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='base-dashboard'),
    path('dashboard/', views.dashboard, name='base-dashboard'),
    path('about/', views.about, name='base-about'),
]
 