import os

from flask import Flask
from flask import Flask,render_template, url_for, flash, redirect, request

import random
import sqlite3

import pandas as pd
import time 
# import pypyodbc
import pyodbc
from flask import Flask
from flask_charts import GoogleCharts, Chart
#from flask_googlecharts import GoogleCharts, BarChart


app = Flask(__name__)
charts = GoogleCharts(app)


@app.route('/enternewfile')
def upload_csv():
   return render_template('upload.html')

@app.route('/question7',methods=['GET','POST'])
def question7():
	return render_template('question7.html')

@app.route('/question7_1',methods=['GET','POST'])
def question7_1():

	conn= sqlite3.connect('Quiz4.db')
	cur = conn.cursor()
	year = int(request.form['year'])
	if year==2010:
	    yr='field2'
	elif year==2011:
	    yr='field3'
	elif year==2012:
	    yr='field4'
	elif year==2013:
	    yr='field5'
	elif year==2014:
	    yr='field6'
	elif year==2015:
	    yr='field7'
	elif year==2016:
	    yr='field8'
	elif year==2017:
	    yr='field9'
	elif year==2018:        
	    yr='field10'
	stateList=[]
	lstate1 = request.form['state1']
	stateList.append(lstate1)
	lstate2 = request.form['state2']
	stateList.append(lstate2)

	lstate3 = request.form['state3']

	stateList.append(lstate3)

	lstate4 = request.form['state4']
	stateList.append(lstate4)

	lstate5 = request.form['state5']
	stateList.append(lstate5)

	lstate6 = request.form['state6']
	stateList.append(lstate6)

	lstate7 = request.form['state7']
	stateList.append(lstate7)

	lstate8 = request.form['state8']
	stateList.append(lstate8)

	lstate9 = request.form['state9']
	stateList.append(lstate9)

	lstate10 = request.form['state10']
	stateList.append(lstate10)

	lstate11 = request.form['state11']
	stateList.append(lstate11)

	lstate12 = request.form['state12']
	stateList.append(lstate12)

	stMain = tuple(stateList)
	print(stMain)
	result=[]
	for var in stMain:
	    cur.execute('SELECT field1,'+yr+' FROM states  WHERE field1 = ?', (var,))
	    max_val = cur.fetchall()
	    result.append(max_val)
	print(result)
	my_chart = Chart("BarChart", "my_chart")
	my_chart.data.add_column("string", "Range")
	my_chart.data.add_column("number", "Count")

	for i in result:
	    iter=[]
	     # col1= str(i[0][1])+"-"+str(i[0][2])
	    if i != []:
	        print(i[0][0])
	        print(i[0][1])

	        iter.append(i[0][0])
	        x=int(i[0][1].replace(',',''))
	        iter.append(x)
	        my_chart.data.add_row(iter)
	print(my_chart)

	 # connectionObject.close()
	conn.close()
	return render_template('question7_1.html',my_chart=my_chart)

@app.route('/q4task7Input',methods=['GET','POST'])
def q4task7Input():
    return render_template('q4task7Input.html')

@app.route('/q4task7',methods=['GET','POST'])
def q4task7():
    conn= sqlite3.connect('Quiz4.db')
    cur = conn.cursor()
    year = int(request.form['year'])
    if year==2010:
        yr='field2'
    elif year==2011:
        yr='field3'
    elif year==2012:
        yr='field4'
    elif year==2013:
        yr='field5'
    elif year==2014:
        yr='field6'
    elif year==2015:
        yr='field7'
    elif year==2016:
        yr='field8'
    elif year==2017:
        yr='field9'
    elif year==2018:
        yr='field10'

    lstate1 = request.form['state1']

    cur.execute('SELECT field2,field3, field4, field5, field6, field7, field8, field9 FROM states  WHERE field1 = ?', (lstate1,))

    my_chart = Chart("ScatterChart", "my_chart")
    #my_chart=PieChart("my_chart")
    my_chart.data.add_column("string", "State")
    my_chart.data.add_column("number", "Population")
    for i in result:
        iter=[]
        # col1= str(i[0][1])+"-"+str(i[0][2])
        if i != []:
            print(i[0][0])
            print(i[0][1])

            iter.append(i[0][0])
            x=int(i[0][1].replace(',',''))
            iter.append(x)
            my_chart.data.add_row(iter)
    print(my_chart)
    # connectionObject.close()
    conn.close()
    return render_template('q4task6.html',my_chart=my_chart)



@app.route('/prevalanceInput',methods=['GET','POST'])
def prevalanceInput():
    return render_template('prevalanceInput.html')

@app.route('/prevalance',methods=['GET','POST'])
def prevalance():
    time1=time.time()
    conn = sqlite3.connect('Quiz3.db')
    Code = request.form['code']
    cur = conn.cursor()
    cur.execute('select * from sp where code= ? order by year',(Code,))
    rows = cur.fetchall()
    # print(rows)
    conn.close()
    time2=time.time()
    TimeTaken= time2-time1
    return render_template('prevalance.html',row=rows,tt=TimeTaken)


@app.route('/chooseCodeOrCountry',methods=['GET','POST'])
def chooseCOC():
    return render_template('chooseCodeOrCountry.html')

@app.route('/optedCodeInput',methods=['GET','POST'])
def OptCodeInp():
    return render_template('optedCodeInput.html')

@app.route('/optedCode',methods=['GET','POST'])
def optedCode():
    time1=time.time()
    conn = sqlite3.connect('Quiz3.db')
    Code = request.form['code']
    cur = conn.cursor()
    cur.execute('select pc.code,pc.entity,pc.year,pc.cost,sp.prevalence from pc inner join sp on pc.entity==sp.entity and pc.year==sp.year where pc.code like ?',(Code,))
    rows = cur.fetchall()
    # print(rows)
    conn.close()
    time2=time.time()
    TimeTaken= time2-time1
    return render_template('optedCode.html',row=rows,tt=TimeTaken)

@app.route('/optedCountryInput',methods=['GET','POST'])
def OptConInp():
    return render_template('optedCountryInput.html')

@app.route('/optedCountry',methods=['GET','POST'])
def optedCountry():
    time1=time.time()
    conn = sqlite3.connect('Quiz3.db')
    entity = request.form['Entity']
    cur = conn.cursor()
    cur.execute('select pc.code,pc.entity,pc.year,pc.cost,sp.prevalence from pc inner join sp on pc.code==sp.code and pc.year==sp.year where pc.entity like ?',(entity,))
    rows = cur.fetchall()
    # print(rows)
    conn.close()
    time2=time.time()
    TimeTaken= time2-time1
    return render_template('optedCountry.html',row=rows,tt=TimeTaken)

@app.route('/costyearinput',methods=['GET','POST'])
def InputCostYear():
    return render_template('costAndYearRangeInput.html')

# @app.route('/cosYeaRangeInput',methods=['GET','POST'])
# def cosYeaRangeInput():
#     return render_template('costAndYearRangeInput.html')

@app.route('/CayRange1',methods=['GET','POST'])
def CayRange1():
    time1 = time.time()
    conn = sqlite3.connect('Quiz3.db')
    cost1 = request.form['cost1']
    cost2 = request.form['cost2']
    year1 = request.form['year1']
    year2 = request.form['year2']
    cur = conn.cursor()
    cur.execute('select pc.code,pc.entity,pc.year,pc.cost,sp.prevalence from pc inner join sp on (pc.code==sp.code and pc.year==sp.year) where (pc.cost >= ? and pc.cost<= ? and pc.year>= ? and pc.year< ?) order by pc.cost',(cost1,cost2,year1,year2,))
    rows = cur.fetchall()
    print(rows)
    conn.close()
    time2=time.time()
    TimeTaken= time2-time1
    return render_template('CayRange1.html',row=rows,tt=TimeTaken)

@app.route('/runqueryinput',methods=['GET','POST'])
def runqueryinput():
    return render_template('runqueryinput.html')

@app.route('/runQuery',methods=['GET','POST'])
def runQuery():
    time1 = time.time()
    conn = sqlite3.connect('Quiz3.db')
    # cost1 = round(random.uniform(1,13),1)
    # cost2 = round(random.uniform(cost1,13),1)
    cost1 = request.form['cost1']
    cost2 = request.form['cost2']
    year1 = request.form['year1']
    year2 = request.form['year2']    
    number = int(request.form['number'])
    cur = conn.cursor()
    for i in range(number):
        cur.execute('select pc.code,pc.entity,pc.year,pc.cost,sp.prevalence from pc inner join sp on (pc.code==sp.code and pc.year==sp.year) where (pc.cost >= ? and pc.cost<= ? and pc.year>= ? and pc.year< ?) order by pc.cost',(cost1,cost2,year1,year2,))
        rows = cur.fetchall()
    time2=time.time()
    TimeTaken= time2-time1
    return render_template('runQuery.html',row=rows,tt=TimeTaken,number=number)

@app.route('/runquerycache',methods=['GET','POST'])
def runquerycache():
    return render_template('runquerycache.html')


port = int(os.getenv('PORT','5000'))
if __name__=='__main__':
    app.run(host='0.0.0.0', port=port,debug= True)

