import os
from flask import *
import sys
import sqlite3
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired
import geopy
import geopy.distance

app = Flask(__name__)
app.config['SECRET_KEY'] = 'la la la'

class NameForm(FlaskForm):
	name = StringField('Name')
	submit = SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def highest_earth_quake():
 	form=NameForm()
 	if form.validate_on_submit():
 		input_name=form.given_name.data
 	connec=sqlite3.connect('data_earth_quakes.db')
 	table_with_data=connec.cursor()
 	table_with_data.execute("SELECT mag, place, id  from q ORDER BY mag desc LIMIT 1")	 		#we will be selecting mag, place, id from table name quakes and sort them in descending order.
 	rows = table_with_data.fetchall()
 	for row in rows:
 		print(row)
 	return render_template('question_5.html',rows=rows,title='')


@app.route('/question7')
def question7():
	connection = sqlite3.connect('data_earth_quakes.db')
	table_with_data = connection.cursor()
	lattitude_first = request.form['lattitude_first']
	lattitude_second = request.form['lattitude_second']
	longitude_first = request.form['longitude_first']
	longitude_second = request.form['longitude_second']
	table_with_data.execute(("SELECT *FROM q WHERE (latitude BETWEEN ? AND ?) AND (longitude BETWEEN ? AND ?)"),(lattitude_first,lattitude_second,longitude_first,longitude_second))
	rows = table_with_data.fetchall()
	for row in rows:
		print(row)
	return render_template('question_7_1.html',title='',rows=rows)

@app.route('/question9',methods=['GET','POST'])
def question9():
	form=NameForm()
	location = request.form['location']
	connec=sqlite3.connect('data_earth_quakes.db')
	table_with_data=connec.cursor()
	table_with_data.execute(("SELECT * from q WHERE locationSource=? ORDER BY time desc LIMIT 4"),(location,))	 		
	attributes = table_with_data.fetchall()
	for att in attributes:
		print(att)
	return render_template('question_9.html',rows=attributes,title='')	


port = int(os.getenv('PORT', '3000'))
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=port, debug=True)
