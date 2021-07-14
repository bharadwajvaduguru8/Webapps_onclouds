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
#import pandas as pd

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'blah blah blah blah'

class NameForm(FlaskForm):
	name = StringField('Name', default="")
	submit = SubmitField('Submit')

'''class IDForm(FlaskForm):
	name = StringField('Please enter ID', default="")
	submit = SubmitField('Submit')

class UpdateForm(FlaskForm):
	name = StringField('Please enter name', default="")
	submit = SubmitField('Submit')
print(os.getenv("PORT"))'''
port = int(os.getenv("PORT", 3000))

@app.route('/')
def food2():
    num1=request.form['num1']
    num2=request.form['num2']
    conn = sqlite3.connect('dba.db')
    cur = conn.cursor()
    sql="select * from food where Price between '"+num1+"'and '"+num2+"'"
    cur.execute(sql)
    result = cur.fetchall()
    conn.commit()
    print (repr(result))
    return render_template('food2.html',result =result)
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=port)
