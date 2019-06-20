from django.db import models
import uuid
import logging
from nsessoracle.utils import get_connection 

logger = logging.getLogger(__name__)

class Tenant(models.Model):
	# pk => tenant.Tenant.pk: (fields.E003) 'pk' is a reserved word that cannot be used as a field name.
	id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
	tenant_name = models.CharField(max_length=20, null=True, blank=True, help_text='Tenant name', unique=True)
	# created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	# updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return str(self.pk) +  ' ~ ' + self.tenant_name.upper()

	def save(self, *args, **kwargs):
		logger.info('Started: creating tenant')
		tenant = self.tenant_name
		password = 'Password123'
		username = 'CFDADMIN'

		logger.log(logging.INFO, 'TENANT - ', tenant, ' | PASSWORD - ', password)

		commands = [
			# GRANT CREATE SESSION TO CFDADMIN;
			f"GRANT CREATE SESSION TO {username}",

			# CREATE SCHEMA schema1 AUTHORIZATION cfdamdin;
			"CREATE USER {tenant} IDENTIFIED BY {password}".format(tenant=tenant, password=password),
		
			# GRANT CONNECT TO SCHEMA1;
			f"GRANT CONNECT TO {tenant}"
		]

		SCHEMA_TABLE_QUOTA_GRANT_QUERY = 'ALTER USER {tenant} quota unlimited on {table_name}'

		SHOW_TABLES_QUERY = """SELECT
			  table_name, owner
			FROM
			  dba_tables
			WHERE
			  owner='CFDADMIN'
			ORDER BY
			  owner, table_name"""

		try:
			con = get_connection()
			cursor = con.cursor()

			# SAVE POINT
			cursor.execute('SAVEPOINT NSE_ORACLE_SAVEPOINT')
			logger.warning('CREATED SAVEPOINT')

			for index, command in enumerate(commands):
				# logger.log(logging.INFO, '(1.%s) EXCECUTING \'' + command + '\'' % (index + 1))
				print('#' * 40)
				cursor.execute(command)

			cursor.execute(SHOW_TABLES_QUERY)
			# Otherwise insertion will fail
			# ALTER USER SCHEMA1 quota unlimited on users;
			for index, tup2 in enumerate(cursor):
				# tup2 -> ('USERS_USER', 'CFDADMIN')
				query = SCHEMA_TABLE_QUOTA_GRANT_QUERY.format(tenant=tenant, table_name=tup2[0])
				logger.warning('-----' + query)
				# logger.info('')
				query = query.format(tup2[0])
				# logging.log(logger.WARNING, '(2.%s) EXCECUTING \'' + query + '\'' % index)
				print('%' * 40)
				cursor.execute(query)

			cursor.close()
			# Object(Tenant) saved
			super().save(*args, **kwargs)
		except Exception as error:
			logger.warning(str(error))
			logger.warning('This object will be unsaved from the database')

			# https://stackoverflow.com/questions/16632243/use-of-rollback-command-in-oracle
			con.execute('ROLLBACK TO NSE_ORACLE_SAVEPOINT') # Rollback
			logger.log('CHANGES ARE ROLLED BACK')
			# import traceback
			# traceback.print_tb(error)
			return
		finally:
			# Close the database connection 
			# logger.info('message') -> won't display the message
			logger.warning('Successfully closed recently opened connection')
			con.close()


class TenantModel(models.Model):
	tenant_name = models.ForeignKey(Tenant, on_delete=models.CASCADE, help_text='Tenant name (FK)')

	class Meta:
		abstract= True

