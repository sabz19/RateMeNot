from flask import Flask,request,render_template
import sys,MySQLdb

app = Flask(__name__)

connection = MySQLdb.connect(host = "localhost",
		user="root",
		passwd="root",
		db="UTD")
cursor = connection.cursor()
database = 'UTD'
@app.route('/')
def home():
	return render_template('Search.html')

@app.route('/results',methods=['GET','POST'])
def search():
	if request.method == 'POST':

		search_query = request.form.get('Search')
		
		cursor = connection.cursor()
		cursor.execute("Select * from course_info limit 10")
		fields = cursor.fetchall()
		return render_template('Search_Results.html',data=fields)


if __name__ == 'main':
	app.run(debug=True)