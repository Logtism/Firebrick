from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


ALLOWED_METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']


class Endpoint:
    def __init_subclass__(cls):
        cls.methods = {}
        # Registering all the methods in the endpoint so we can quickly check if the endpoint has a method handler
        for method in ALLOWED_METHODS:
            if method in cls.__dict__:
                cls.methods[method] = cls.__dict__[method]

    @classmethod
    @csrf_exempt
    def handler(cls, request, *args, **kwargs):
        # Check if the method is in the endpoint and if not return a not allowed method msg
        if request.method in cls.methods:
            response = cls.methods[request.method](request, *args, **kwargs)
            # Check what type the return of the endpoint 
            if type(response) == dict:
                return JsonResponse(response)
            elif type(response) == tuple:
                return JsonResponse(response[0], status=response[1])
            else:
                return response
        else:
            # Return a function so if the user wants a custom response they can override the functions in the endpoint class
            return cls.not_allowed(request, *args, **kwargs)
    
    @classmethod
    def not_allowed(cls, request, *args, **kwargs):
        return JsonResponse({'success': False, 'error_message': 'Method is not allowed.'}, status=405)