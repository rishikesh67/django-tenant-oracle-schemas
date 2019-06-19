def get_tenant(request):
	# cfd.nseinvestease.com:8000
	host = request.get_host()
	tenant = None
	parts = host.split(':')
	l = len(parts) 
	if l == 1:
		host = parts[0]
	elif l == 2:
		host, port = parts

	if host:
		host_parts = host.split('.')

		if host_parts:
			tenant = host_parts[0]

	return tenant
