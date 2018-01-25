""" 
	Program to login to utdallas web page and retrieve all related HTML PAGE
"""

import requests,lxml.html
import os
from lxml import etree
from bs4 import BeautifulSoup

"""
	The login url is a redirect from the base url 
"""
BASE_URL = "https://provost.utdallas.edu/ues-report/table/term_17f,col_ecs,heat_none"

LOGIN_PAGE = requests.get(BASE_URL)
LOGIN_URL = LOGIN_PAGE.url

session = requests.Session()
login = session.get(LOGIN_URL)

login_html = lxml.html.fromstring(login.text)
hidden_inputs = login_html.xpath(r'//form//input[@type = "hidden"]')


#Fetch all hidden form parameters

form = {x.attrib["name"]:x.attrib["value"] for x in hidden_inputs}
form['netid'] = '##########'
form['password'] = '########'

response = session.post(LOGIN_URL,data = form)

RESULT_PAGE = session.get(BASE_URL)


# Fetch all table information and store it in a text file for later processing 
# This essentially entails the course/professor data required

soup = BeautifulSoup(RESULT_PAGE.text,'lxml')
table = soup.find('table')
table_rows = table.find_all('tr')


path  = os.getenv("HOME") + "/Desktop/scrap.txt"
f = open(path,'w')

for row in table_rows:
	for table_data in row:
		f.write(str(table_data))
	f.write("\n")
