from django.test import TestCase
from firebrick.tests import ResolveUrlTest, GetViewTest
from . import views


class TestHome(TestCase, ResolveUrlTest, GetViewTest):
    name = 'base-dashboard'
    view = views.dashboard
    template = 'base/dashboard.html'
    status = 200
    

class TestAbout(TestCase, ResolveUrlTest, GetViewTest):
    name = 'base-about'
    view = views.about
    template = 'base/about.html'
    status = 200