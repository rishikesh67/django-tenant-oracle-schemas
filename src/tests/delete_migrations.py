import os
import glob
import shutil

def delete_migrations(dir_path='/Users/hygull/Projects/Python3/DjangoTenantOracleSchemas/django-tenant-oracle-schemas/src'):
	dir_path = os.path.join(os.path.abspath(dir_path))
	print(dir_path)
	
	if os.path.isdir(dir_path):
		files = os.listdir(dir_path)

		for file in files:
			abspath = os.path.join(dir_path, file)
			if os.path.isdir(abspath):
				if file == 'migrations':
					print('Found migration as ', abspath)
					shutil.rmtree(abspath)

					print(abspath, ' is removed')
				else:
					print('Iteration over -> ', abspath)
					delete_migrations(abspath)
			else:
				print('Skipping files')
	else:
		print('Path is not a directory')
