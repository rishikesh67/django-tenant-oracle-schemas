from django.db import models
import uuid
import logging

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
		tenant = self.tenant_name
		password = 'Password123'
		username = 'CFDADMIN'

		logger.info('TENANT - ', tenant, ' | PASSWORD - ', password)

		commands = [
			# GRANT CREATE SESSION TO CFDADMIN;
			f"GRANT CREATE SESSION TO {username}",

			# CREATE SCHEMA schema1 AUTHORIZATION cfdamdin;
			"CREATE USER {tenant} IDENTIFIED BY {password}".format(tenant=tenant, password=password)
		
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
			import cx_Oracle;
			DBNAME = "orcl"
			DBUSER = 'cfdadmin'
			DBPASSWORD = 'pandora123$321#'
			DBHOST = 'cfduat.c0be6oyqiohf.ap-south-1.rds.amazonaws.com'

			# postgresql://cfdadmin@cfduat.c0be6oyqiohf.ap-south-1.rds.amazonaws.com/orcl
			DBPATH = '{username}/{password}@{host}/{db_name}'.format(
																	username=DBUSER, 
																	password=DBPASSWORD, host=DBHOST,
			                                                        db_name=DBNAME
			                                                    )
			# https://cx-oracle.readthedocs.io/en/latest/installation.html
			con = cx_Oracle.connect(DBUSER, DBPASSWORD, f"{DBHOST}/{DBNAME}")
			cursor = con.cursor()

			for index, command in enumerate(commands):
				logger.info('(1.%s) EXCECUTING \'' + command + '\'' % (index + 1))
				cursor.execute(command)

			cursor.execute(SHOW_TABLES_QUERY)
			# Otherwise insertion will fail
			# ALTER USER SCHEMA1 quota unlimited on users;
			query = SCHEMA_TABLE_QUOTA_GRANT_QUERY.format(tenant=tenant)
			for index, tup2 in enumerate(cursor):
				# tup2 -> ('USERS_USER', 'CFDADMIN')
				logging.info(table)
				query = query.format(tup2[0])
				logging.info('(2.%s) EXCECUTING \'' + query + '\'' % index)
				cursor.execute(query)

			cursor.close()
			# Object(Tenant) saved
			super().save(*args, **kwargs)
		except Exception as error:
			logger.warning(str(error))
			logger.warning('This object will be unsaved from the database')
			return
		finally:
			# Close the database connection
			logger.info('Successfully closed recently opened connection')
			con.close()


class TenantModel(models.Model):
	tenant_name = models.ForeignKey(Tenant, on_delete=models.CASCADE, help_text='Tenant name (FK)')

	class Meta:
		abstract= True

