from django.urls import path
from . import views


urlpatterns = [
    path('test_endpoint/', views.test_endpoint.handler, name='api-test-endpoint'),
    path('test_argparser/one_not_required/', views.test_argparse_one_not_required.handler, name='api-argparser-one-not-required'),
    path('test_argparser/one_required/', views.test_argparse_one_required.handler, name='api-argparser-one-required'),
    path('test_serializer_data/', views.test_serializer_data_view.handler, name='api-test-serializer-data'),
    path('test_serializer_parse/', views.test_serializer_parse_view.handler, name='api-test-serializer-parse'),
]