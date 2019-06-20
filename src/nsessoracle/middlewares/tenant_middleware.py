from django.http import HttpResponse, JsonResponse
from nsessoracle.utils import get_tenant, get_connection 
from tenants.models import Tenant
from users.models import User
import logging

logger = logging.getLogger(__name__)

class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info('Inside TenantMiddleware')
        logger.info(request)

        # --- BEFORE ---
        is_main_domain, tenant = get_tenant(request)
        logger.info('TENANT - ', tenant)

        if tenant:
            if tenant != 'nseinvestease':
                tenant_obj = Tenant.objects.filter(tenant_name=tenant).first()
                if tenant_obj:
                    con = get_connection()
                    cursor = con.cursor()
                    # tenant -> schema
                    # ALTER SESSION SET CURRENT_SCHEMA = SCHEMA2;
                    SET_SCHEMA_QUERY = 'ALTER SESSION SET CURRENT_SCHEMA = {tenant}'.format(tenant=tenant)
                    logger.log(logging.ERROR, SET_SCHEMA_QUERY)
                    cursor.execute(SET_SCHEMA_QUERY)
                else:
                    if not is_main_domain:
                        return JsonResponse({
                            'message': 'Could not find this tenant ' + tenant,
                            'status': 400
                        })

        response = self.get_response(request)
        # --- AFTER ---

        return response
