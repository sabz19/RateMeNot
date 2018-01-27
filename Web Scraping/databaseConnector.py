""" Program to connect to local database and dump the collected data """

import MySQLdb

db = MySQLdb.connect(host = "localhost",
					 user = "root"
					 passwd = "root"
					 db = "UTD")

#Cursor object to execute queries
cur = db.cursor()