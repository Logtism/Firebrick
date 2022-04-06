from django.test import TestCase
from .models import Person


class TestAssertObjectExists(TestCase):
    def setUp(self):
        self.person = Person.objects.create(name='test1')
        
    def test_object_does_not_exist(self):
        try:
            self.assertObjectExists(Person, id=2)
            self.fail("'assertObjectExists' said object exists that does not exist")
        except AssertionError:
            pass
        
    def test_objects_does_exist(self):
        self.assertObjectExists(Person, id=1)
        

class TestAssertObjectDoesNotExist(TestCase):
    def setUp(self):
        self.person = Person.objects.create(name='test1')
        
    def test_object_does_exist(self):
        try:
            self.assertObjectDoesNotExist(Person, id=1)
            self.fail("'assertObjectDoesNotExist' said object does not exists that does exists")
        except AssertionError:
            pass
        
    def test_objects_does_not_exist(self):
        self.assertObjectDoesNotExist(Person, id=2)