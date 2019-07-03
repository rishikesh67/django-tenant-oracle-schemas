from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from tenants.models import Tenant
from .serializers import TenantSerializer
import logging


# FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
# logging.basicConfig(format=FORMAT)

logger = logging.getLogger(__name__)

class TenantRegister(APIView):

	def post(self, request, *args, **kwargs):
		status, message, response = 200, 'Successfully created tenant', {}
		data = request.data
		logger.info('In tenant creator view')
		logger.info('tenant_name')
		tenant_name = data.get('tenant_name')
		print(data)
		print(tenant_name)

		try:
			print(Tenant.objects.filter(tenant_name=tenant_name))
			tenant = Tenant.objects.filter(tenant_name=tenant_name).first()

			print(tenant)

			if tenant:
				message = 'Tenant is already registered'
			else:
				if request.is_main_domain and tenant_name is not None:
					tenant = Tenant.objects.create(tenant_name=tenant_name)
				elif tenant_name is None:
					message = "Tenant name cannot be None"
				else:
					message = "Registration is not possible from tenant domain"
		except Exception as error:
			message = str(error)

		response['status'] = status
		response['message'] = message
		return Response(response)
	
	def get(self, request, *args, **kwargs):
		tenants = Tenant.objects.all()
		serializer = TenantSerializer(tenants, many=True)
		return Response(serializer.data)

		# >>> for text in strings:
		# ...     m = re.match(r'(\w+.)?nseinvestease.com', text)
		# ...     print(m)
		# ... 
		# <_sre.SRE_Match object; span=(0, 21), match='cfd.nseinvestease.com'>
		# <_sre.SRE_Match object; span=(0, 22), match='nmf2.nseinvestease.com'>
		# <_sre.SRE_Match object; span=(0, 22), match='nmf3.nseinvestease.com'>
		# None
		# >>> 
		# >>> for text in strings:
		# ...     m = re.match(r'(\w+.)?nseinvestease.com', text)
		# ...     if m:
		# ...         print(m.groups())
		# ... 
		# ('cfd.',)
		# ('nmf2.',)
		# ('nmf3.',)
		# >>> 
		# >>> strings.append('nseinvestease.com')
		# >>> 
		# >>> strings
		# ['cfd.nseinvestease.com', 'nmf2.nseinvestease.com', 'nmf3.nseinvestease.com', 'mysql.jdbc.dotnet', 'nseinvestease.com']
		# >>> 
		# >>> for text in strings:
		# ...     m = re.match(r'(\w+.)?nseinvestease.com', text)
		# ...     if m:
		# ...         print(m.groups())
		# ... 
		# ('cfd.',)
		# ('nmf2.',)
		# ('nmf3.',)
		# (None,)
		# >>> 
		# >>> 