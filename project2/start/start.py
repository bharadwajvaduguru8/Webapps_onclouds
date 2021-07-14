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


#ROUTES!
@app.route('/',methods=['GET','POST'])
def homePage():
	form=NameForm()
	name=form.name.data
	return render_template('start.html',title='',name_on_HTML=name)

port = int(os.getenv('PORT', '3000'))
app.run(host='0.0.0.0', port=port)