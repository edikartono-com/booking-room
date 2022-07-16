from django.conf import settings
class CrossDomainSession:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        if response.cookies:
            host = request.get_host()
            if host not in settings.SESSION_COOKIE_DOMAIN:
                domain = ".{domain}".format(domain=host)
                for cookie in response.cookies:
                    if domain in response.cookies[cookie]:
                        response.cookies[cookie]['domain'] = domain
        return response