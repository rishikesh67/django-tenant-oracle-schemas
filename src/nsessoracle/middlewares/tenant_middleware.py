from django.http import HttpResponse, JsonResponse
from nsessoracle.utils import get_tenant

class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('Inside TenantMiddleware')
        print(request)

        # --- BEFORE ---
        tenant = get_tenant(request)
        print('TENANT - ', tenant)
        response = self.get_response(request)
        # --- AFTER ---

        return response