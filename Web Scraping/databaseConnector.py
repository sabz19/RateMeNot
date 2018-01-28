""" Program to connect to local database and dump the collected data """
from __future__ import print_function
import MySQLdb
import os
import unicodedata

try:
	db = MySQLdb.connect(host = "localhost",
						 user = "root",
						 passwd = "root",
						 db = "UTD")
except:
	raise ValueError("Bad connection given")

#Cursor object to execute queries
cur = db.cursor()

#Open file containing the scraped values from web
#path  = os.getenv("HOME") + "/Desktop/scraped.txt"
path = os.getcwd() + "/scraped.txt"

with open(path,"r") as file:
	for line in file:
		
		if not line.strip():  #if row is empty move on 
			continue
		# Data is ';'' separated
		line_split = line.split(";")
		insert_values = []
		line_len = len(line_split)
		for index,word in enumerate(line_split):
			
			if index == line_len - 1:
				word = word[:-1] # remove ',' from last word
			if not word.strip() or index == 10:  # column 10 is redundant
				continue
			
			# check if the string is a float type
			# If not, then encapsulate string in quotes
			try:
				float(word)
			except:
				word = '"' + word + '"'
			insert_values.append(word)
		
		seq = ",".join(insert_values)
		
		# Insert list of values obtained in one go
		cur.execute("INSERT into course_info values (%s);" %seq)
		

db.commit()
cur.close()
db.close()