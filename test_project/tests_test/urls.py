from django.urls import path
from . import views


urlpatterns = [
    path('get_view/', views.get_view, name='tests-test-get-view'),
    path('get_view_or_404/<int:id>/', views.get_or_404, name='tests-test-get_or_404'),
    path('login_view/', views.login_view, name='tests-test-login-view')
]