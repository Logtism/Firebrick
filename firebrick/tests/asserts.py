from django.test import TestCase


def assertObjectExists(self, model, **filters):
    if not model.objects.filter(**filters).first():
        filter_str = ''
        for filter_ in filters:
            filter_str += f'{filter_} = {filters[filter_]} & '
        raise AssertionError(f'Object with filter(s) \'{filter_str[:-3]}\' not created.')
    
    
def assertObjectDoesNotExist(self, model, **filters):
    if model.objects.filter(**filters).first():
        filter_str = ''
        for filter_ in filters:
            filter_str += f'{filter_} = {filters[filter_]} & '
        raise AssertionError(f'Object with filter(s) \'{filter_str[:-3]}\' created.')
    
    
TestCase.assertObjectExists = assertObjectExists
TestCase.assertObjectDoesNotExist = assertObjectDoesNotExist