""" 
	Program to login to utdallas web page and retrieve all related HTML PAGE
	and write to file for further processing
"""
from __future__ import print_function
from bs4 import BeautifulSoup

import requests,lxml.html
import os
"""
	The login url is a redirect from the base url 
"""
BASE_URL = "https://provost.utdallas.edu/ues-report/table/term_17f,heat_none"

LOGIN_PAGE = requests.get(BASE_URL)
LOGIN_URL = LOGIN_PAGE.url

session = requests.Session()
login = session.get(LOGIN_URL)

login_html = lxml.html.fromstring(login.text)
hidden_inputs = login_html.xpath(r'//form//input[@type = "hidden"]')


#Fetch all hidden form parameters

form = {x.attrib["name"]:x.attrib["value"] for x in hidden_inputs}
form['netid'] = '######'
form['password'] = '######'

response = session.post(LOGIN_URL,data = form)

RESULT_PAGE = session.get(BASE_URL)


# Fetch all table information and store it in a text file for later processing 
# This essentially entails the course/professor data required

soup = BeautifulSoup(RESULT_PAGE.text,'lxml')
table = soup.find('table')
table_rows = table.find_all('tr')

#Open file for HTML page to be written in 

#path  = os.getenv("HOME") + "/Desktop/scraped.txt"
path = os.getcwd() + "/scraped.txt"
file = open(path,'w')

# Go through all the rows in the html table
# Fetch table data for each row

for row in table_rows:
	table_data = row.find_all('td')	
	
	for index,td in enumerate(table_data):

		# We dont want the first index or last or status UES Reported
		if(index == 0 or index == 15 or td.text == "reported"): 
			continue

		# if the given table data contains a link, fetch the hyper link text alone
		# There is a better method to do this with bs	
		link_index = td.text.find('a href')
		if(link_index != -1):
			first_close_tag = td.text.find('>',link_index)
			second_open_tag = td.text.find('<',first_close_tag)
			keyword = td[first_close_tag + 1:second_open_tag]
			file.write(keyword.text.strip() + ';')
		else:	
			file.write(td.text.strip() + ';')
	file.write("\n")
		
file.close()