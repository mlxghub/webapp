from django.utils.deprecation import MiddlewareMixin


class Testmiddle(MiddlewareMixin):
    def process_request(self, request):
        pass

    def process_view(self, request, callback, callback_args, callback_kwargs):
        pass

    def process_exception(self, request, exception):
        pass

    def process_response(self, request, response):
        return response


class Nextmiddle(MiddlewareMixin):
    def process_request(self, request):
        pass

    def process_view(self, request, callback, callback_args, callback_kwargs):
        pass

    def process_exception(self, request, exception):
        pass

    def process_response(self, request, response):
        return response