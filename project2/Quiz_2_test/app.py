from flask import *
import sqlite3
import os
import shutil
import pandas as pd
import sys
from datetime import date,timedelta
import datetime
import pathlib
from wtforms import StringField, IntegerField, SubmitField, SelectField
from flask_wtf import FlaskForm
from math import sin, cos, sqrt, atan2, radians

app = Flask(__name__)

app.config['SECRET_KEY'] = 'blah blah blah blah'

def_lat=radians(32.729641)
def_lon=radians(-97.110566)
R_earth = 6373.0

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/total',methods=["POST"])
def total():
	con=sqlite3.connect("./static/quakes.db")
	net=request.form['net_value']
	curss=con.execute("select count(*) from q where net=?",(net,))
	count=curss.fetchall()
	curss=con.execute("select place,id,max(magNst) from q where net=?",(net,))
	max_va=curss.fetchall()
	curss=con.execute("select place,id,min(magNst) from q where net=?",(net,))
	min_va=curss.fetchall()
	return render_template("index.html",min=min_va,max=max_va,count=count[0][0])


class quakeBox(FlaskForm):
	lat1=StringField("")
	lon1=StringField("")
	lat2=StringField("")
	lon2=StringField("")
	mag=StringField("")
	submit=SubmitField("")

@app.route('/retrieve', methods=["POST"])
def retrieve():
	form = quakeBox()
	if form.validate_on_submit():
		Loc_lat1 = request.form['lat1']
		Loc_lat2 = request.form['lon1']
		Loc_long1 = request.form['lat2']
		Loc_long2 = request.form['lon2']
		loc_mag = request.form['mval']
		conn = sqlite3.connect('Quiz2.db')
		cur = conn.cursor()
		cur.execute('select count(*) from q where (latitude between ? and ?) and (longitude between ? and ?)',(Loc_lat1,Loc_lat2,Loc_long1,Loc_long2,))
		rows = cur.fetchall()
		cur.execute('select place, latitude, longitude, max(mag) from q where (mag < ?) and (latitude between ? and ?) and (longitude between ? and ?)',(loc_mag,Loc_lat1,Loc_lat2,Loc_long1,Loc_long2,))
		Maxval = cur.fetchall()
		cur.execute('select place, latitude, longitude, min(mag) from q where (mag < ?) and (latitude between ? and ?) and (longitude between ? and ?)',(loc_mag,Loc_lat1,Loc_lat2,Loc_long1,Loc_long2,))
		minval = cur.fetchall()
		# print(len(rows))
		print(rows)
		conn.close()
		return render_template('show.html',form=form,row=rows,Max=Maxval,min=minval)
	return render_template('index.html',form=form,name=None)

@app.route('/mag',methods=["POST"])
def mag():
	inp=request.form['idloc']
	dis=request.form['dist']
	con=sqlite3.connect("./static/quakes.db")
	curss=con.execute("select * from q;")
	row=curss.fetchall()
	mag=[]
	for i in row:
		if inp==i[10] or inp in i[11]:
			dlon = def_lon - radians(i[2])
			dlat = def_lat - radians(i[1])
			a = sin(dlat / 2)**2 + cos(def_lat) * cos(radians(i[1])) * sin(dlon / 2)**2
			c = 2 * atan2(sqrt(a), sqrt(1 - a))

			distan=R_earth * c
			if distan<200:
				mag.append(i[4])
			elif(len(mag)!=0):
				avg=sum(mag)//len(mag)
				mag.append(avg)
			else:
				mag.append(4)
		elif(len(mag)!=0):
			avg=sum(mag)//len(mag)
			mag.append(avg)
		else:
			mag.append(4)
	inde1=mag.index(max(mag))
	inde2=mag.index(min(mag))
	lat1=row[inde1][1]
	lon1=row[inde1][2]
	lat2=row[inde2][1]
	lon2=row[inde2][2]
	dep1=row[inde1][3]
	dep2=row[inde2][3]
	dat1=row[inde1][0]
	dat2=row[inde2][0]
	pl1=row[inde1][11]
	pl2=row[inde2][11]
	return render_template("index.html",pl1=pl1,pl2=pl2,mag1=max(mag),mag2=min(mag),lat1=lat1,lat2=lat2,lon1=lon1,lon2=lon2,dat1=dat1,dat2=dat2,id1=dep1,id2=dep2,UID=1001747270,Name="Sai Sri Harsha Panchumarthy")

@app.route('/get_mag',methods=["POST"])
def get_mag():
	con=sqlite3.connect("./static/quakes.db")
	curs=con.execute("select * from q;")
	row=curs.fetchall()
	mag1=float(request.form['mag1'])
	mag2=float(request.form['mag2'])
	loc=request.form['idloc']
	index=[]
	for i in row:
		if loc in i[11]:
			if float(i[4])>=mag1 and float(i[4])<=mag2:
				index.append(i)
	return render_template("index.html",quakes=index)

port = int(os.getenv('PORT',"3000"))
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=port,debug = True)