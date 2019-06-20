from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from tenants.models import Tenant

import logging
logger = logging.getLogger(__name__)


def request(self):
	return render(request, 'tests/drop.html', {})

class TenantCreateView(APIView):

	def post(self, request, *args, **kwargs):
		status, message, response = 200, 'Successfully created tenant', {}
		data = request.data
		logger.info('In tenant creator view')
		logger.info('tenant_name')
		tenant_name = data.get('tenant_name')
		tenant = Tenant.objects.filter(tenant_name=tenant_name).first()

		if tenant:
			message = 'Tenant is already registered'
		else:
			tenant = Tenant.objects.create(tenant_name=tenant_name)

		response['status'] = status
		response['message'] = message
		return Response(response)
	
