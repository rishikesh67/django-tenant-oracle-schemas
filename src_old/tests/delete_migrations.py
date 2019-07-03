import os
import glob
import shutil
import logging

# logging.basicConfig(level=logging.DEBUG)
# DEBUG:root:Skipping file /Users/hygull/Projects/Python3/DjangoTenantOracleSchemas/django-tenant-oracle-schemas/src/tenants/models.py


# logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
# 2019-06-24 16:19:29,898 Skipping file /Users/hygull/Projects/Python3/DjangoTenantOracleSchemas/django-tenant-oracle-schemas/src/manage.py


# logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG, datefmt='%d/%m/%Y %H:%M:%S %p')
# 24/06/2019 04:23:31 PM Skipping file /Users/hygull/Projects/Python3/DjangoTenantOracleSchemas/django-tenant-oracle-schemas/src/manage.py

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG, datefmt='[%d/%m/%Y %H:%M:%S %p] =>')
# 24/06/2019 16:24:02 PM Skipping file /Users/hygull/Projects/Python3/DjangoTenantOracleSchemas/django-tenant-oracle-schemas/src/manage.py

def delete_migrations(
		dir_path='/Users/hygull/Projects/Python3/DjangoTenantOracleSchemas/django-tenant-oracle-schemas/',
		migrations=True,
		pycaches=False,
		**kwargs
	):
	dir_path = os.path.join(os.path.abspath(dir_path))
	logging.info(dir_path)
	
	if os.path.isdir(dir_path):
		files = os.listdir(dir_path)

		for file in files:
			abspath = os.path.join(dir_path, file)
			if os.path.isdir(abspath):
				logging.debug('file ---> {0} {1}'.format(file, pycaches))
				if (migrations and file == 'migrations') or (pycaches and file == "__pycache__"):
					logging.debug('Found migration as ' + abspath)
					shutil.rmtree(abspath)
					logging.debug(abspath + ' is removed')
				else:
					logging.debug('Iteration over -> ' + abspath)
					delete_migrations(abspath, pycaches, migrations, **kwargs)
			else:
				logging.debug('Skipping file ' + abspath)
	else:
		logging.debug('Path is not a directory')

