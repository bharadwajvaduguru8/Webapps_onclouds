import os
import time
from flask import *
import sys
import sqlite3
import redis 
import hashlib
import json
import random

app = Flask(__name__)
#app.config['SECRET_KEY'] = 'la la la'

r = redis.StrictRedis(host='bhara.redis.cache.windows.net',port=6380,password='WiHEHM1F+vB718mqFSPbsR6XreXEHNQPPyhGYajZtes=', ssl=True) 



#Qestion 6
@app.route("/question6",methods=['GET','POST'])
def question6():
  return render_template('question6.html')
@app.route("/question6_1",methods=['GET','POST'])
def question6_1():
  connec=sqlite3.connect('database.db')
  table_with_data=connec.cursor()
  magup=request.form['magup']
  magdown=request.form['magdown']
  time1=time.time()
#table_with_data.execute("select sp.Entity,sp.Code,sp.Year,sp.Prevalence,pc.Cost from sp,pc where ((sp.Code=?) or (sp.Entity=?)) order by sp.Year ",(input1,input1,))
  table_with_data.execute("select latitude,longitude,mag,id from q where (mag>?) and (mag<?) ",(magdown,magup,))
  attributes = table_with_data.fetchall() 
  #print("hello")
  time2=time.time()
  time_c=time2-time1 
  return render_template("question6_1.html",time=time_c,attributes=attributes)


#question 7
@app.route("/question7",methods=['GET','POST'])
def question7():
  return render_template('question7.html')
@app.route("/question7_1",methods=['GET','POST'])
def question7_1():
  connec=sqlite3.connect('database.db')
  table_with_data=connec.cursor()
  magup=request.form['magup']
  magdown=request.form['magdown']
  dvalue=request.form['dvalue']
  time1=time.time()
  
  magu=int(magup)
  magd=int(magdown)
  dval=float(dvalue)
  a=round(random.uniform(magd, magu), 1)
  up_value=a+dval
  down_value=a-dval
#table_with_data.execute("select sp.Entity,sp.Code,sp.Year,sp.Prevalence,pc.Cost from sp,pc where ((sp.Code=?) or (sp.Entity=?)) order by sp.Year ",(input1,input1,))
  table_with_data.execute("select latitude,longitude,mag,id from q where (mag>?) and (mag<?) ",(down_value,up_value,))
  attributes = table_with_data.fetchall() 
  #print("hello")
  time2=time.time()
  time_c=time2-time1 
  return render_template("question7_1.html",time=time_c,attributes=attributes)


#question 8
@app.route("/question8",methods=['GET','POST'])
def question8():
  return render_template('question8.html')
@app.route("/question8_1",methods=['GET','POST'])
def question8_1():
  connec=sqlite3.connect('database.db')
  magup=request.form['magup']
  magdown=request.form['magdown']
  dvalue=request.form['dvalue']
  input1=request.form['numberof']
  time1=time.time()
  magu=int(magup)
  magd=int(magdown)
  dval=float(dvalue)
#table_with_data.execute("s
  for i in range(1,int(input1)+1,1):
    a=float(round(random.uniform(magd, magu), 1))
    up_value=a+dval
    down_value=a-dval
    table_with_data=connec.cursor()
    #table_with_data.execute("select sp.Entity,sp.Code,sp.Year,sp.Prevalence,pc.Cost from sp,pc where ((sp.Code=?) or (sp.Entity=?)) order by sp.Year ",(input1,input1,))
    table_with_data.execute("select latitude,longitude,mag,id from q where (mag>?) and (mag<?) ",(down_value,up_value,))
    attributes = table_with_data.fetchall() 
  #print("hello")
  time2=time.time()
  time_c=time2-time1 
  return render_template("question8_1.html",time=time_c,attributes=attributes,input1=input1)





#question 9
@app.route("/question9",methods=['GET','POST'])
def question11():
  return render_template('question9.html')
@app.route("/question9_1",methods=['GET','POST'])
def question9_1():
  connec=sqlite3.connect('database.db')
  input1=request.form['input1']
  value=request.form['value']
  magup=request.form['magup']
  magdown=request.form['magdown']
  dvalue=request.form['dvalue']
  magu=int(magup)
  magd=int(magdown)
  dval=float(dvalue)
  time_c=0
  a=float(round(random.uniform(magd, magu), 1))
  up_value=a+dval
  down_value=a-dval
  val=int(down_value)
  for H in range(0,int(val)):
    if input1.lower()=='c':
        if r.exists("all"):
          time1=time.time()
          result = json.loads(r.get("all"))
          time2=time.time()
          time_c = time_c+(time2-time1)
        else:
          time1 = time.time()
          table_with_data=connec.cursor()
          table_with_data.execute("select latitude,longitude,mag,id from q where (mag>?) and (mag<?) ",(down_value,up_value,))
          output = table_with_data.fetchall()
          time2=time.time()
          time_c = time_c+(time2-time1)
          result = []
          for row in output:
            result.append(row[0])
          r.set("all", json.dumps(result))
    else:
      time1 = time.time()
      table_with_data=connec.cursor()
      table_with_data.execute("select latitude,longitude,mag,id from q where (mag>?) and (mag<?) ",(down_value,up_value,))
      output = table_with_data.fetchall()
      time2=time.time()
      time_c = time_c + (time2-time1)
      result = []
      for row in output:
        result.append(row[0])
  time_c = time_c * 1000
  return render_template('question11_1.html', value=value, time_c=time_c)





if __name__ == '__main__':
  app.run()