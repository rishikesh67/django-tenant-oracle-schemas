def drop_tables(con, query):
	print(con.version)
	# con = cx_Oracle.connect(DBPATH)
	cursor = con.cursor()

	print('CURSOR ', cursor)

	print('(DROP TABLES) EXECUTING QUERY -> ', query)
	cursor.execute(query)
	# l = [row for row in rows]

	# print(l)
	for statement in cursor:
		# ('DROP TABLE "MASTERDATA_LOCATION" CASCADE CONSTRAINTS;',)
		# print(statement)

		statement = statement[0].strip(';')
		# print(statement)
		# DROP TABLE "MASTERDATA_LOCATION" CASCADE CONSTRAINTS
		cur = con.cursor()

		cur.execute(statement)
		cur.close()
		print('Successfully executed query - {' + statement + '}')
