from django.http import HttpResponse, JsonResponse
from nsessoracle.utils import get_tenant, get_connection 
from tenants.models import Tenant
from users.models import User
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)

class TenantMiddleware:
    """
    Tenant Middleware
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('Inside TenantMiddleware')
        print(request)

        # --- BEFORE ---
        print('Getting tenant')
        is_main_domain, tenant = get_tenant(request)
        print('TENANT - ', tenant)
        print('IS MAIN DOMAIN', is_main_domain)
        print(is_main_domain, tenant, type(tenant))

        request.is_main_domain = is_main_domain
        request.is_local_domain = False

        if tenant:
            print('ok')
            if tenant != 'nseinvestease' and tenant != '127':
                print('here')
                request.tenant = Tenant.objects.filter(tenant_name=tenant).first()
                print(request.tenant)
            else:
                print('here 2')
                if request.is_main_domain is not True and tenant == '127':
                    print('yes')
                    request.is_local_domain = True
                else:
                    print('no')

                request.tenant = None
        else:
            request.tenant = None

        if is_main_domain:
            print('Is main domain')
            
            if not request.path.startswith('/tests/register') and (not request.path.startswith('/tests/users/')) and (not (request.path == '/')) and (not request.path.startswith("/admin/")) and (not request.path.startswith('/register/')) :
                return JsonResponse({
                    'status': 400,
                    "message": 'Main domain is only allowed to register tenants not other activities'
                })
        elif not request.tenant:
            print('Not a tenant')

            return JsonResponse({
                'status': 400,
                "message": 'Could not find this tenant'
            })


        print('Tenant is set as ', request.tenant, request.is_local_domain, request.is_main_domain)

        response = self.get_response(request)

        # --- AFTER ---
        return response
