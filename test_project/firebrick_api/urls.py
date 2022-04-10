from django.urls import path
from . import views


urlpatterns = [
    path('test_endpoint/', views.test_endpoint.handler, name='api-test-endpoint'),
]