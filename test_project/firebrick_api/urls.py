from django.urls import path
from . import views


urlpatterns = [
    path('test_endpoint/', views.test_endpoint.handler, name='api-test-endpoint'),
    path('test_argparser/one_not_required/', views.test_argparse_one_not_required.handler, name='api-argparser-one-not-required')
]