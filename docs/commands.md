### List all tables

```sql
SELECT
  table_name, owner
FROM
  dba_tables
WHERE
  owner='CFDADMIN'
ORDER BY
  owner, table_name
```

```bash
"AUTH_GROUP"	"CFDADMIN"
"AUTH_GROUP_PERMISSIONS"	"CFDADMIN"
"AUTH_PERMISSION"	"CFDADMIN"
"AUTH_USER"	"CFDADMIN"
"AUTH_USER_GROUPS"	"CFDADMIN"
"AUTH_USER_USER_PERMISSIONS"	"CFDADMIN"
"DJANGO_ADMIN_LOG"	"CFDADMIN"
"DJANGO_CONTENT_TYPE"	"CFDADMIN"
"DJANGO_MIGRATIONS"	"CFDADMIN"
"DJANGO_SESSION"	"CFDADMIN"
"TENANTS_TENANT"	"CFDADMIN"
"USERS_USER"	"CFDADMIN"
```

### List all schemas

> **Ref:** https://support.chartio.com/knowledgebase/how-to-list-all-available-schemas

```sql
select USERNAME from SYS.ALL_USERS;
```

```bash
"XS$NULL"
"SYSKM"
"SYSDG"
"SYSBACKUP"
"CFD"
"SCHEMA2"
"SCHEMA1"
"CFDADMIN"
"RDSADMIN"
"CTXSYS"
"GSMCATUSER"
"ANONYMOUS"
"XDB"
"APPQOSSYS"
"DBSNMP"
"DIP"
"GSMUSER"
"GSMADMIN_INTERNAL"
"OUTLN"
"SYSTEM"
"AUDSYS"
"SYS"
```

### Drop Schema (but you have to delete USER)

```sql
DROP USER CFD;
```

```bash
Query 1 OK: 

```