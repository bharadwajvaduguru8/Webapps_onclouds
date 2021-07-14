import os
import shutil
import csv
import sys
from flask import Flask,render_template, url_for, flash, redirect, request
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from flask_bootstrap import Bootstrap
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired
import sqlite3
from werkzeug import secure_filename
import pandas as pd

app = Flask(__name__)
bootstrap = Bootstrap(app)

# Configurations
app.config['SECRET_KEY'] = 'blah blah blah blah'

class NameForm(FlaskForm):
	name = StringField('Name', default="")
	submit = SubmitField('Submit')

class IDForm(FlaskForm):
	name = StringField('Please enter ID', default="")
	submit = SubmitField('Submit')

class UpdateForm(FlaskForm):
	name = StringField('Please enter name', default="")
	submit = SubmitField('Submit')	


#ROUTES!
@app.route('/',methods=['GET','POST'])
def homePage():
	return render_template('homepage.html')
	# return render_template('homepage_loc.html')

@app.route('/imageofselection',methods=['GET','POST'])
def index():
	form = NameForm()
	if form.validate_on_submit():
		name = form.name.data
		conn = sqlite3.connect('Assign1.db')
		cur = conn.cursor()
		cur.execute('select Picture from names where Name= ?',(name,))
		rows = cur.fetchall()
		# print(len(rows))
		# print(rows)
		if(rows[0][0]==None):
			rows=["No data available"]
		return render_template('imageofselection.html',form=form,name=name,row=rows)
	return render_template('index.html',form=form,name=None)

@app.route('/updatedetails',methods=['GET','POST'])
def index1():
	form = UpdateForm()
	if form.validate_on_submit():
		nameUp = form.name.data
		conn = sqlite3.connect('Assign1.db')
		cur = conn.cursor()
		cur.execute('update names set Room= ? where Name= ?',(name,))
		rows = cur.fetchall()
		print(len(rows))
		print(rows)
		if(rows[0][0]==None):
			rows=["No data available"]
		return render_template('imageofselection.html',form=form,name=name,row=rows)
	return render_template('index.html',form=form,name=None)

@app.route('/idselection',methods=['GET','POST'])
def idselection():
	form = IDForm()
	if form.validate_on_submit():
		ID = form.name.data
		conn = sqlite3.connect('Assign1.db')
		cur = conn.cursor()
		cur.execute('select Picture,Caption from names where ID= ?',(ID,))
		rows = cur.fetchall()
		# if(rows[0][0]==None & rows[0][1]==None):
		# 	rows=["not available"]
		# elif(rows[0][0])==None):
		# 	rows[0][0]=["No image available"]
		# elif(rows[0][1]==None):
		# 	rows[0][1]=["No Caption"]
		# else:
		# 		pass
		return render_template('idandcaptionselection.html',form=form,name=ID,row=rows)
	return render_template('index.html',form=form,name=None)

@app.route('/enternew')
def upload_csv():
   return render_template('upload.html')

@app.route('/upload_file',methods = ['POST', 'GET'])
def upload_file():
   if request.method == 'POST':
       con = sqlite3.connect('Assign1.db')
       csv = request.files['myfile']
       filename=secure_filename(csv.filename)
       file = pd.read_csv(csv)
       file.to_sql('names2', con, schema=None, if_exists='replace', index=True, index_label=None, chunksize=None, dtype=None)	  
       con.close()
       return render_template("file_upload.html",msg = filename)

@app.route('/list',methods=['GET','POST'])
def list1():
		conn = sqlite3.connect('Assign1.db')
		cur = conn.cursor()
		cur.execute('select * from Assign1_DB')
		rows = cur.fetchall()
		return render_template("list.html",rows = rows)

@app.route('/salary',methods=['GET','POST'])
def salary():
		conn = sqlite3.connect('Assign1.db')
		cur = conn.cursor()
		cur.execute('select * from people1')
		rows=cur.fetchall()
		return render_template("salary.html",row=rows)

@app.route('/help')
def help():
	text_list = []
	# Python Version
	text_list.append({
		'label':'Python Version',
		'value':str(sys.version)})
	# os.path.abspath(os.path.dirname(__file__))
	text_list.append({
		'label':'os.path.abspath(os.path.dirname(__file__))',
		'value':str(os.path.abspath(os.path.dirname(__file__)))
		})
	# OS Current Working Directory
	text_list.append({
		'label':'OS CWD',
		'value':str(os.getcwd())})
	# OS CWD Contents
	label = 'OS CWD Contents'
	value = ''
	text_list.append({
		'label':label,
		'value':value})
	return render_template('help.html',text_list=text_list,title='help')

@app.errorhandler(404)
@app.route("/error404")
def page_not_found(error):
	return render_template('404.html',title='404')

@app.errorhandler(500)
@app.route("/error500")
def requests_error(error):
	return render_template('500.html',title='500')

port = int(os.getenv('PORT', '3000'))
app.run(host='0.0.0.0', port=port)