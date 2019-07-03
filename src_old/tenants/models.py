from django.db import models
import uuid
import logging
from nsessoracle.utils import get_connection 
from tests.makemigrations_and_migrate import makemigrations_and_migrate
import os
from django.conf import settings

logger = logging.getLogger(__name__)



class TenantManager(models.Manager):
    def get_queryset(self):
        print("Inside Model Manager's Code")
        tenant_users = User.objects.filter(tenant_name=request.tenant)
        return tenant_users


class Tenant(models.Model):
    # pk => tenant.Tenant.pk: (fields.E003) 'pk' is a reserved word that cannot be used as a field name.
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4) # Primary key
    tenant_name = models.CharField(max_length=20, null=False, blank=True, help_text='Tenant name', unique=True) # Tenant name
    # created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    # updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return str(self.pk) +  ' ~ ' + self.tenant_name.upper()

    # def save(self, *args, **kwargs):
    #     logger.info('Started: creating tenant')
    #     tenant = self.tenant_name
    #     password = 'Password123'
    #     username = 'CFDADMIN'

    #     logger.log(logging.INFO, 'TENANT - ', tenant, ' | PASSWORD - ', password)

    #     commands = [
    #         # GRANT CREATE SESSION TO CFDADMIN;
    #         f"GRANT CREATE SESSION TO {username}",

    #         # CREATE SCHEMA schema1 AUTHORIZATION cfdamdin;
    #         "CREATE USER {tenant} IDENTIFIED BY {password}".format(tenant=tenant, password=password),
        
    #         # GRANT CONNECT TO SCHEMA1;
    #         f"GRANT CONNECT TO {tenant}"
    #     ]

    #     SCHEMA_TABLE_QUOTA_GRANT_QUERY = 'ALTER USER {tenant} quota unlimited on {table_name}'

    #     SHOW_TABLES_QUERY = """SELECT
    #           table_name, owner
    #         FROM
    #           dba_tables
    #         WHERE
    #           owner='CFDADMIN'
    #         ORDER BY
    #           owner, table_name"""


    #     # ALTER SESSION SET CURRENT_SCHEMA = SCHEMA2;
    #     SET_SCHEMA_QUERY_MAIN = 'ALTER SESSION SET CURRENT_SCHEMA = {tenant}'

    #     # from django.conf import settings
    #     # import json
    #     # logger.warning('--- DATABASES ---')
    #     # databases = settings.DATABASES
    #     # logger.warning(json.dumps(databases, indent=4))
    #     # old_user = databases['default']['USER']
    #     # old_password =  databases['default']['PASSWORD']

    #     logger.warning('Currently selected schema is %s' % (tenant))
    #     try:
    #         con = get_connection()
    #         cursor = con.cursor()

    #         # SAVE POINT
    #         cursor.execute('SAVEPOINT NSE_ORACLE_SAVEPOINT')
    #         logger.warning('CREATED SAVEPOINT')

    #         for index, command in enumerate(commands):
    #             # logger.log(logging.INFO, '(1.%s) EXCECUTING \'' + command + '\'' % (index + 1))
    #             logger.warning(command)
    #             cursor.execute(command)

    #         SET_SCHEMA_QUERY = SET_SCHEMA_QUERY_MAIN.format(tenant=tenant)
    #         logger.warning(SET_SCHEMA_QUERY)
    #         cursor.execute(SET_SCHEMA_QUERY)

    #         cursor.execute(SHOW_TABLES_QUERY)


    #         # databases['default']['USER'] = tenant
    #         # databases['default']['PASSWORD'] = 'Password123'

    #         # print('NEW DB', settings.DATABASES)
            
    #         # MAKE MIGRATIONS & MIGRATE
    #         this_dir = os.path.dirname(os.path.abspath(__file__))
    #         mm_commands = [
    #             "python3 manage.py makemigrations users",
    #             "python3 manage.py makemigrations tenants",
    #             'python3 manage.py makemigrations tests',
    #             "python3 manage.py migrate"
    #         ]
    #         project_root = '/Users/hygull/Projects/Python3/DjangoTenantOracleSchemas/django-tenant-oracle-schemas/src'
            
    #         makemigrations_and_migrate(project_root, this_dir, mm_commands)

    #         logger.warning('Successfully created & applied migrations')

    #         # # Otherwise insertion will fail
    #         # # ALTER USER SCHEMA1 quota unlimited on users;
    #         # for index, tup2 in enumerate(cursor):
    #         #     # tup2 -> ('USERS_USER', 'CFDADMIN')
    #         #     query = SCHEMA_TABLE_QUOTA_GRANT_QUERY.format(tenant=tenant, table_name=tup2[0])
    #         #     logger.debug(query)
    #         #     # logger.info('')
    #         #     query = query.format(tup2[0])
    #         #     # logging.log(logger.WARNING, '(2.%s) EXCECUTING \'' + query + '\'' % index)
    #         #     print('%' * 40)
    #         #     cursor.execute(query)

    #         # # Change back to `CFDADMIN`
    #         # SET_SCHEMA_QUERY = SET_SCHEMA_QUERY_MAIN.format(tenant='CFDADMIN')
    #         # logger.debug(SET_SCHEMA_QUERY)
    #         # cursor.execute(SET_SCHEMA_QUERY)
    #         # logger.warning('Now we are done...')

    #         print('Closing cursor')
    #         cursor.close()
    #         # Object(Tenant) saved
    #         super().save(*args, **kwargs)
    #     except Exception as error:
    #         logger.warning(str(error))
    #         logger.warning('This object will be unsaved from the database')

    #         # https://stackoverflow.com/questions/16632243/use-of-rollback-command-in-oracle
    #         cursor.execute('ROLLBACK TO NSE_ORACLE_SAVEPOINT') # Rollback
    #         logger.warning('CHANGES ARE ROLLED BACK')
    #         # import traceback
    #         # traceback.print_tb(error)
    #         return
    #     finally:
    #         # settings.DATABASES["USER"] = old_user
    #         # settings.DATABASES["PASSWORD"] = old_password

    #         logger.warning('Reverted back all the changes (settings)')
    #         logger.warning(settings.DATABASES)
    #         # Close the database connection 
    #         # logger.info('message') -> won't display the message
    #         logger.warning('Successfully closed recently opened connection')
    #         con.close()
    #         print('---' * 30)


class TenantModel(models.Model):
    tenant_name = models.ForeignKey(Tenant, on_delete=models.CASCADE, help_text='Tenant name (FK)')

    class Meta:
        abstract= True

