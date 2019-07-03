class TenantDataMixin(object):
	"""
	TenantDataMixin
	===============
		- A Mixin to provide tenant specific data from any model

		- Data will be tenant specific 

		- E.g. in case of users, all users that belong to any specific tenant 
	"""

	def get_data(self, request, Model, *args, many=False, **filters):
		queryset = Model.objects.filter(tenant_name=request.tenant, **filters)

		if many:
			# For many/multiple objects
			print('A request for many/multiple objects')
			result = queryset
		else:
			# For a single object
			print('A request for a single object')
			result = queryset.first()

		return result
