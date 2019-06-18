def show_tables(con, query):
	cursor = con.cursor()

	cursor.execute(query)

	for table in cursor:
		print(table)

	cursor.close()


	"""
		(venv3.6.7) ➜  tests git:(master) ✗ python oracle-connect.py 4
		('AUTH_GROUP', 'CFDADMIN')
		('AUTH_GROUP_PERMISSIONS', 'CFDADMIN')
		('AUTH_PERMISSION', 'CFDADMIN')
		('AUTH_USER', 'CFDADMIN')
		('AUTH_USER_GROUPS', 'CFDADMIN')
		('AUTH_USER_USER_PERMISSIONS', 'CFDADMIN')
		('DJANGO_ADMIN_LOG', 'CFDADMIN')
		('DJANGO_CONTENT_TYPE', 'CFDADMIN')
		('DJANGO_MIGRATIONS', 'CFDADMIN')
		('DJANGO_SESSION', 'CFDADMIN')
		('TENANTS_TENANT', 'CFDADMIN')
		('USERS_USER', 'CFDADMIN')
	"""
