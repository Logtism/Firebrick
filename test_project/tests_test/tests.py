from django.test import TestCase
from django.core.management import call_command
import shutil
import os
from firebrick.tests.test import ResolveUrlTest, GetViewTest, GETViewOr404Test, GETLoginRequiredTest
from . import views


class ResolveUrlTesting(TestCase, ResolveUrlTest):
    name = 'tests-test-get-view'
    view = views.get_view


class GetViewTesting(GetViewTest):
    name = 'tests-test-get-view'
    view = views.get_view
    template = 'tests_test/get_view.html'
    status = 200


class GetViewTestingCustomAsserts(TestCase, GetViewTest):
    name = 'tests-test-get-view'
    view = views.get_view
    template = 'tests_test/get_view.html'
    status = 400

    def get_view_test_asserts(self, response):
        # Nothing in here cause I can't think of anything that would work here
        pass


class TestGetOr404Testing(TestCase, GETViewOr404Test):
    name = 'tests-test-get_or_404'
    view = views.get_view

    fixtures = ['tests_test/fixtures/tests_test/person.json']

    success_args = [2]
    success_status = 200
    success_template = 'tests_test/get_or_404.html'

    fail_args = [1000]
    fail_status = 404


class TestGetOr404TestingCustomAsserts(TestCase, GETViewOr404Test):
    name = 'tests-test-get_or_404'
    view = views.get_view

    fixtures = ['tests_test/fixtures/tests_test/person.json']

    success_args = [2]
    success_status = 404
    success_template = 'tests_test/get_or_404.html'

    fail_args = [1000]
    fail_status = 200

    def get_view_or_404_test_asserts_fail(self, response):
        pass

    def get_view_or_404_test_asserts_success(self, response):
        pass


class TestLoginRequired(TestCase, GETLoginRequiredTest):
    name = 'tests-test-login-view'
    view = views.login_view
    template = 'tests_test/login_view.html'
    status = 200


class TestLoginRequiredCustomAsserts(TestCase, GETLoginRequiredTest):
    name = 'tests-test-login-view'
    view = views.login_view
    template = 'tests_test/login_view.html'
    status = 400

    def get_login_required_asserts_success(self, response):
        pass