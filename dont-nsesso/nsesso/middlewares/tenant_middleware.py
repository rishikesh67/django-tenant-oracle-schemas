from django.http import HttpResponse, JsonResponse
from nsesso.utils import get_tenant # , get_connection 
from tenants.models import Tenant
from users.models import User
import logging
from django.shortcuts import redirect

logger = logging.getLogger(__name__)

class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        status, message, response = 400, 'Bad request', {}
        logger.debug('Inside TenantMiddleware')
        logger.debug(request)

        # --- BEFORE ---
        is_main_domain, tenant = get_tenant(request)
        logger.debug('TENANT - ' + tenant)

        throw_bad_req = True
        if tenant:
            if tenant != 'nseinvestease':
                tenant_obj = Tenant.objects.filter(tenant_name=tenant).first()
                if tenant_obj:
                    request.tenant = tenant
                    throw_bad_req = False
                else:
                    message = 'Tenant %s is not registered' % (tenant)
        else:
            message = 'You are not authorised to access this domain'

        if throw_bad_req:
            response["message"] = message
            response["status"] = status
            return JsonResponse(response)

        # cookies = request.COOKIES
        # print(cookies)
        # user = cookies.get('user')
        if request.path == '/login/' or request.path.startswith('/login/'):
            if user:
                return redirect('tests:tests-tenants')
        else:
            if not user:
                return redirect('tests:tests-login')

        response = self.get_response(request)

        # --- AFTER ---
        return response
