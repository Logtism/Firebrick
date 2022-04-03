from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


ALLOWED_METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']


class EndPoint:
    methods = {}

    def __init_subclass__(cls):
        for method in ALLOWED_METHODS:
            if method in cls.__dict__:
                cls.methods[method] = cls.__dict__[method]

    @csrf_exempt
    def handler(self, request, *args, **kwargs):
        if request.method in self.methods:
            response = self.methods[request.method](self, request, *args, **kwargs)
            if type(response) == dict:
                return JsonResponse(response)
            elif type(response) == tuple:
                return JsonResponse(response[0], status=response[1])
            else:
                return response
        else:
            return self.not_allowed_method(request)

    def not_allowed_method(self, request):
        return JsonResponse({'success': False, 'error_message': 'Method is not allowed.'}, status=405)