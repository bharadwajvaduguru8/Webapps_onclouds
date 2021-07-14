import pypyodbc
from flask import Flask, request, render_template
import json
from json import loads, dumps
import redis

app = Flask(__name__)

r = redis.StrictRedis(
    host='assignmnt3.redis.cache.windows.net',
    port=6380,
    password='eCLtprHAm7shQaOIQOYeNu6xBmCMvKLuw+CWLBVPec8=', ssl=True)

conn = pypyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                        'SERVER=tcp:earth123.database.windows.net;'
                        'PORT=1433;'
                        'DATABASE=earth123;'
                        'UID=nithya;'
                        'PWD=Rita@123')
# Enter Server, UID and PWD. Deleted for security purposes
cursor = conn.cursor()


@app.route('/')
def home():
    return render_template('home.html')

# @app.route("/showpie", methods=["POST", "GET"])
# def showpie():
#     category = str(request.form.get('category', ''))
#     query1 = "SELECT * FROM groc WHERE category = '" + str(category) + "'"
#     cursor.execute(query1)
#     r1 = cursor.fetchall()
#     return render_template('showpie.html',category=category,rows=r1)

#user enter category veg or nonveg and display all results of that category - pie chart
#quiz 0a
#CHECKKKKKKKKKKKKKKKK
@app.route("/showpiechart", methods=["POST", "GET"])
def showpiechart():
    query1 = "SELECT * FROM voting WHERE StateName  = 'ALASKA'"
    cursor.execute(query1)
    r1 = cursor.fetchall()

    query2 = "SELECT * FROM voting WHERE StateName  = 'ILLINOIS'"
    cursor.execute(query2)
    r2 = cursor.fetchall()

    rows1 = ([
        ['Item','Quantity'],
        [r1[0][0],r1[0][2]],
        [r1[1][0],r1[1][2]],
        [r1[2][0],r1[2][2]]
        ])
        
    rows2 = ([
        ['Item','Quantity'],
        [r2[0][0],r2[0][2]],
        [r2[1][0],r2[1][2]]
        ])

    return render_template('showpie.html', rows1=rows1, rows2=rows2)

#5-perfect--jus display info 
@app.route("/basic", methods=["POST", "GET"])
def basic():
    query1 = "select StateName from voting where totalpop between 2000 and 8000"
    cursor.execute(query1)
    r1 = cursor.fetchall()

    query2 = "select StateName from voting where totalpop between 8000 and 40000"
    cursor.execute(query2)
    r2 = cursor.fetchall()

    return render_template('basic.html', rows1=r1, rows2=r2)

#6-perfect---give range as 1 or 2 
@app.route('/regscatter', methods=['POST', 'GET'])
def regscatter():
    m1 = int(request.form.get('m1', ''))
    m2 = int(request.form.get('m2', ''))
    m1 = m1 * 1000
    m2 = m2 * 1000


    query1 = "SELECT sum(Registered) FROM voting WHERE TotalPop BETWEEN '"+str(m1)+"' AND '"+str(m2)+"'"
    cursor.execute(query1)
    s1 = cursor.fetchall()


    rows = ([
        ['reg', 'pop'],
        [str(m1)+'-'+str(m2), s1[0][0]]
        ])
    return render_template('regscatter.html', rows1=rows)

#7-perfect give range as 100
@app.route("/quiz7", methods=["POST", "GET"])
def quiz7():
    range1 = int(request.form.get('range',''))
    rangeStart = 0
    rangeEnd = range1
    maxQuery = "Select max(totalpop) from voting"
    cursor.execute(maxQuery)
    maxResult = cursor.fetchall()
    maxPopulation = maxResult[0][0]
    storeResult = []
    start = []
    end = []
    counter = 0
    while rangeStart < maxPopulation:
        query = "Select count(statename) from voting where totalpop between '" +str(rangeStart)+ "' and '" +str(rangeEnd)+"'"
        cursor.execute(query)
        resultSet = cursor.fetchall()
        countResult = resultSet[0][0]
        storeResult.append(countResult)
        start.append(rangeStart)
        end.append(rangeEnd)
        rangeStart = rangeEnd
        rangeEnd = rangeEnd + range1
        counter = counter + 1
    list_a = []
    list_a.append(['Population Range','Number of States'])
    for i in range(0,counter):
        list_a.append([str(start[i]) + '-' + str(end[i]),storeResult[i]])
    return render_template('quizpie.html',rows=list_a)

# 8-perefct give range as 1 or 2 
# horizontal bar graph show number on each digit generated
@app.route("/horizontalbar", methods=["POST", "GET"])
def horizontalbar():

 

    r1 = []
    range1 = int(request.form.get('range', ''))
    range1 = range1+1
    for i in range(range1):
        modulo = (i**3)%10
        r1.append(modulo)
    
    r2=[]
    
    for i in range(range1):
        count=r1.count(r1[i])
        r2.append(count)
    
    rows = []
    rows.append(['Range Value', 'Number of Times'])
    
    for i in range(0,range1):
        rows.append([r1[i],r2[i]])
    
    return render_template('bar.html', rows=rows)
#perfect-jus list the count why arent the values working
@app.route("/list", methods=["POST", "GET"])
def list():
    # depthrange1 = float(request.form.get('depthrange1', ''))
    # query1="SELECT * FROM earthq WHERE latitude >= '" + str(latitude1) + "' AND latitude <= '" + str(latitude2) + "' AND longitude >= '" + str(longitude1) + "' AND longitude <= '" + str(longitude2) + "'"
    locationSource = str(request.form.get('locationSource', ''))
    range1 = request.form.get('range1', '')
    range2 = request.form.get('range2', '')
    range3 = request.form.get('range3', '')
    range4 = request.form.get('range4', '')
    range5 = request.form.get('range5', '')
    range6 = request.form.get('range6', '')

    query1 = "SELECT count * FROM earthq WHERE locationSource = '" + str(locationSource) + "' AND mag between '" + str(range1) + "' AND '" + str(range2) + "'"
    cursor.execute(query1)
    r1 = cursor.fetchall()

    query2 = "SELECT count(*) FROM earthq WHERE locationSource = '" + str(locationSource) + "' AND mag between '" + str(
        range3) + "' AND '" + str(range4) + "'"
    cursor.execute(query2)
    r2 = cursor.fetchall()

    query3 = "SELECT count(*) FROM earthq WHERE locationSource = '" + str(locationSource) + "' AND mag between '" + str(
        range5) + "' AND '" + str(range6) + "'"
    cursor.execute(query3)
    r3 = cursor.fetchall()
    return render_template('list.html', rows1=r1, rows2=r2, rows3=r3)


@app.route("/showpie", methods=["POST", "GET"])
def showpie():
    locationSource = str(request.form.get('locationSource', ''))
    range1 = int(request.form.get('range1', ''))
    range2 = int(request.form.get('range2', ''))
    range3 = int(request.form.get('range3', ''))
    range4 = int(request.form.get('range4', ''))
    range5 = int(request.form.get('range5', ''))
    range6 = int(request.form.get('range6', ''))

    query1 = "SELECT count(*) FROM earthq WHERE locationSource = '" + str(locationSource) + "' AND mag between '" + str(range1) + "' AND '" + str(range2) + "'"
    cursor.execute(query1)
    r1 = cursor.fetchall()

    query2 = "SELECT count(*) FROM earthq WHERE locationSource = '" + str(locationSource) + "' AND mag between '" + str(
        range3) + "' AND '" + str(range4) + "'"
    cursor.execute(query2)
    r2 = cursor.fetchall()

    query3 = "SELECT count(*) FROM earthq WHERE locationSource = '" + str(locationSource) + "' AND mag between '" + str(
        range5) + "' AND '" + str(range6) + "'"
    cursor.execute(query3)
    r3 = cursor.fetchall()

    rows = ([
        ['Magnitude', 'Number of quakes'],
        [str(range1) + '-' + str(range2), r1[0][0]],
        [str(range3) + '-' + str(range4), r2[0][0]],
        [str(range5) + '-' + str(range6), r3[0][0]]

    ])

    return render_template('showpie.html', rows1=r1,rows2=r2,rows3=r3)


@app.route("/pie", methods=["POST", "GET"])
def pie():
    locationSource = str(request.form.get('locationSource', ''))
    range1 = float(request.form.get('range1', ''))
    range2 = float(request.form.get('range2', ''))
    range3 = float(request.form.get('range3', ''))
    range4 = float(request.form.get('range4', ''))
    range5 = float(request.form.get('range5', ''))
    range6 = float(request.form.get('range6', ''))

    query1 = "SELECT count(*) FROM earthq WHERE locationSource = '" + str(locationSource) + "' AND mag between '" + str(
        range1) + "' AND '" + str(range2) + "'"
    cursor.execute(query1)
    r1 = cursor.fetchall()

    query2 = "SELECT count(*) FROM earthq WHERE locationSource = '" + str(locationSource) + "' AND mag between '" + str(
        range3) + "' AND '" + str(range4) + "'"
    cursor.execute(query2)
    r2 = cursor.fetchall()

    query3 = "SELECT count(*) FROM earthq WHERE locationSource = '" + str(locationSource) + "' AND mag between '" + str(
        range5) + "' AND '" + str(range6) + "'"
    cursor.execute(query3)
    r3 = cursor.fetchall()

    rows1 = ([
        ['Magnitude', 'Number of Earthquakes'],
        [str(range1) + '-' + str(range2), r1[0][0]],
        [str(range3) + '-' + str(range4), r2[0][0]],
        [str(range5) + '-' + str(range6), r3[0][0]]
    ])

    query8 = "select count(*) from earthq where mag > 5.0 and deptherror > 5"
    cursor.execute(query8)
    r8 = cursor.fetchall()
    query9 = "select count(*) from earthq where mag > 5.0 and deptherror < 5"
    cursor.execute(query9)
    r9 = cursor.fetchall()

    rows2 = ([
        ['Magnitude and Depth Error', 'Number of Earthquakes'],
        ['Depth Error > 5', r8[0][0]],
        ['Depth Error < 5', r9[0][0]]

    ])

    return render_template('pie.html', rows=[rows1, rows2])


@app.route("/bar", methods=["POST", "GET"])
def bar():
    locationSource = str(request.form.get('locationSource', ''))
    range1 = float(request.form.get('range1', ''))
    range2 = float(request.form.get('range2', ''))
    range3 = float(request.form.get('range3', ''))
    range4 = float(request.form.get('range4', ''))
    range5 = float(request.form.get('range5', ''))
    range6 = float(request.form.get('range6', ''))

    query1 = "SELECT count(*) FROM earthq WHERE locationSource = '" + str(locationSource) + "' AND mag between '" + str(
        range1) + "' AND '" + str(range2) + "'"
    cursor.execute(query1)
    r1 = cursor.fetchall()

    query2 = "SELECT count(*) FROM earthq WHERE locationSource = '" + str(locationSource) + "' AND mag between '" + str(
        range3) + "' AND '" + str(range4) + "'"
    cursor.execute(query2)
    r2 = cursor.fetchall()

    query3 = "SELECT count(*) FROM earthq WHERE locationSource = '" + str(locationSource) + "' AND mag between '" + str(
        range5) + "' AND '" + str(range6) + "'"
    cursor.execute(query3)
    r3 = cursor.fetchall()

    rows = ([
        ['Magnitude', 'Number of Earthquakes'],
        [str(range1) + '-' + str(range2), r1[0][0]],
        [str(range3) + '-' + str(range4), r2[0][0]],
        [str(range5) + '-' + str(range6), r3[0][0]]
    ])

    return render_template('bar.html', rows=rows)

@app.route("/scatter", methods=["POST", "GET"])
def scatter():
    locationSource = str(request.form.get('locationSource', ''))
    range1 = float(request.form.get('range1', ''))
    range2 = float(request.form.get('range2', ''))
    range3 = float(request.form.get('range3', ''))
    range4 = float(request.form.get('range4', ''))
    range5 = float(request.form.get('range5', ''))
    range6 = float(request.form.get('range6', ''))

    query1 = "SELECT count(*) FROM earthq WHERE locationSource = '" + str(locationSource) + "' AND mag between '" + str(
        range1) + "' AND '" + str(range2) + "'"
    cursor.execute(query1)
    r1 = cursor.fetchall()

    query2 = "SELECT count(*) FROM earthq WHERE locationSource = '" + str(locationSource) + "' AND mag between '" + str(
        range3) + "' AND '" + str(range4) + "'"
    cursor.execute(query2)
    r2 = cursor.fetchall()

    query3 = "SELECT count(*) FROM earthq WHERE locationSource = '" + str(locationSource) + "' AND mag between '" + str(
        range5) + "' AND '" + str(range6) + "'"
    cursor.execute(query3)
    r3 = cursor.fetchall()

    rows = ([
        ['Magnitude', 'Number of Earthquakes'],
        [str(range1) + '-' + str(range2), r1[0][0]],
        [str(range3) + '-' + str(range4), r2[0][0]],
        [str(range5) + '-' + str(range6), r3[0][0]]
    ])

    return render_template('scatter.html', rows=rows)


@app.route("/line", methods=["POST", "GET"])
def line():
    locationSource = str(request.form.get('locationSource', ''))
    range1 = float(request.form.get('range1', ''))
    range2 = float(request.form.get('range2', ''))
    range3 = float(request.form.get('range3', ''))
    range4 = float(request.form.get('range4', ''))
    range5 = float(request.form.get('range5', ''))
    range6 = float(request.form.get('range6', ''))

    query1 = "SELECT count(*) FROM earthq WHERE locationSource = '" + str(locationSource) + "' AND mag between '" + str(
        range1) + "' AND '" + str(range2) + "'"
    cursor.execute(query1)
    r1 = cursor.fetchall()

    query2 = "SELECT count(*) FROM earthq WHERE locationSource = '" + str(locationSource) + "' AND mag between '" + str(
        range3) + "' AND '" + str(range4) + "'"
    cursor.execute(query2)
    r2 = cursor.fetchall()

    query3 = "SELECT count(*) FROM earthq WHERE locationSource = '" + str(locationSource) + "' AND mag between '" + str(
        range5) + "' AND '" + str(range6) + "'"
    cursor.execute(query3)
    r3 = cursor.fetchall()

    rows = ([
        ['Magnitude', 'Number of Earthquakes'],
        [str(range1) + '-' + str(range2), r1[0][0]],
        [str(range3) + '-' + str(range4), r2[0][0]],
        [str(range5) + '-' + str(range6), r3[0][0]]
    ])

    return render_template('line.html', rows=rows)


if __name__ == '__main__':
    app.run()
