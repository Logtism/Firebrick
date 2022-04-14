from django.test import TestCase
from django.http import Http404
from .models import Person


class TestGetObjectOr404(TestCase):
    def setUp(self):
        self.person = Person.objects.create(name='test1')
        
    def test_not_created_id(self):
        try:
            Person.objects.get_object_or_404(id=100)
            self.fail("'get_object_or_404' did not error when given a id that does not exist.")
        except Http404:
            pass
        
    def test_created_id(self):
        self.assertEquals(Person.objects.get_object_or_404(id=self.person.id), self.person)
        
    def test_created_id_and_username(self):
        self.assertEquals(Person.objects.get_object_or_404(id=self.person.id, name=self.person.name), self.person)