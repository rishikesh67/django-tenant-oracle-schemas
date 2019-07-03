import cx_Oracle;

def get_connection():
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

	# Returning connection object
	return con