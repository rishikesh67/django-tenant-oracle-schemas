import logging

logger = logging.getLogger(__name__)

# def get_tenant(request):
# 	# cfd.nseinvestease.com:8000
# 	host = request.get_host()
# 	logger.info(host)
# 	tenant = None
# 	is_main_domain = False
# 	parts = host.split(':')
# 	l = len(parts) 

# 	if l == 1:
# 		front = parts[0]
# 	elif l == 2:
# 		front, port = parts

# 	if front:
# 		# cfd.nseinvestease.com
# 		front_parts = front.split('.')

# 		if len(front_parts) == 2:
# 			is_main_domain = True

# 		tenant = front_parts[0]

# 	logger.info('Tenant - ', tenant)
# 	return is_main_domain, tenant


def get_tenant(request):
	print('Inside get tenant')
	# cfd.nseinvestease:8000
	host = request.get_host()
	print('HOST', host)
	tenant = None
	is_main_domain = False

	parts = host.split(':')
	l = len(parts) 
	print(parts)

	if l == 1:
		front = parts[0]
	elif l == 2:
		front, port = parts

	if front:
		# cfd.nseinvestease
		front_parts = front.split('.')
		print(front_parts)

		if len(front_parts) == 2 and front_parts[1] == 'nseinvestease':
			tenant = front_parts[0]
		elif len(front_parts) == 1:
			is_main_domain = True
			
	logger.info('Tenant - ', tenant)
	return is_main_domain, tenant


	