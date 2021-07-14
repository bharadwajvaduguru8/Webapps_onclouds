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
class NameForm1(FlaskForm):
	lattitude_first = StringField('Lattitude of first location')
	longitude_first = StringField('longitude of first location')
	lattitude_second = StringField('Lattitude of second location')
	longitude_second = StringField('longitude of second location')
	submit = SubmitField('Submit')
class quakeRange(FlaskForm):
	Mag1 = StringField('Enter the Magnitude 1 ', default="")
	Mag2 = StringField('Enter the Magnitude 2 ', default="")
	Par = StringField('Enter the number of partitions expected')
	submit = SubmitField('Submit')
@app.route('/', methods=["GET"])
def hello_world():
    obj = {}
    conn = sqlite3.connect('data_earth_quakes.db')
    cur = conn.cursor()
    cur.execute("""SELECT * FROM q where net not null order by magNst desc limit 1 """, ())
    
    result= cur.fetchall()
    minnet = result[0]
    reslen = len(result)                        
    return render_template('index.html', result=minnet, len=reslen)

port = int(os.getenv('PORT', '3000'))
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=port, debug=True)