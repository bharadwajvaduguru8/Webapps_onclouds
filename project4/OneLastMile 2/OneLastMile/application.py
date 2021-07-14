import pypyodbc
from flask import Flask, request, render_template
import sys,os
import json
from json import loads, dumps

app = Flask(__name__)

conn = pypyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=nilam.database.windows.net;DATABASE=neelamdb1;UID=nilam.database.windows.net;PWD=Birdy2112.')
# Enter Server, UID and PWD. Deleted for security purposes
cursor = conn.cursor()


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index', methods=["POST", "GET"])
def index():

    # success="SELECT   Registered , count(Registered) AS number from (SELECT CASE when Registered BETWEEN 0 and 9000 then 10000 WHEN Registered between 10000 and 19000 then 20000 WHEN Registered between 20000 and 29000 then 30000 ELSE 100 END AS Registered from voting_i) T  GROUP BY T.Registered"
    success = "SELECT  mag , count(mag) AS number from (SELECT CASE when mag BETWEEN '3' and '4' then '3 to 4' WHEN mag between '4' and '5' then '4 to 5' WHEN mag between '5' and '6' then '5 to 6' ELSE '6+' END AS mag from QUAKES1) T  GROUP BY T.mag"
    cursor.execute(success)

    result_set = cursor.fetchall()
    state=[]
    print(result_set)
    for row in result_set:
        state.append(row[0])
        state.append(row[1])

    return render_template('index.html', ci=state)

@app.route('/index1', methods=["POST", "GET"])
def index1():
    range1 = str(request.form.get('range1', ''))
    range2 = int(request.form.get('range2', ''))
    range3 = int(request.form.get('range3', ''))
    # success="SELECT   Registered , count(Registered) AS number from (SELECT CASE when Registered BETWEEN 0 and 9000 then 10000 WHEN Registered between 10000 and 19000 then 20000 WHEN Registered between 20000 and 29000 then 30000 ELSE 100 END AS Registered from voting_i) T  GROUP BY T.Registered"
    # success = "SELECT  latitude , count(latitude) AS number from (SELECT CASE when latitude BETWEEN '10' and '20' then '10 to 20' WHEN latitude between '20' and '30' then '20 to 30' WHEN latitude between '30' and '40' then '30 to 40' WHEN latitude between '40' and '50' then '40 to 50' ELSE '50+' END AS latitude from QUAKES1 where net ='" + str(net) + "') T  GROUP BY T.latitude"
    # success = "SELECT  mag , count(mag) AS number from (SELECT CASE when mag BETWEEN '3' and '4' then '3 to 4' WHEN mag between '4' and '5' then '4 to 5' WHEN mag between '5' and '6' then '5 to 6' ELSE '6+' END AS mag from QUAKES1 where mag ='" + str(range1) + "') T  GROUP BY T.mag"
    success = "SELECT  mag, count(mag) AS number  from (SELECT CASE when mag BETWEEN '0' and '1' then '0 to 1' WHEN mag between '1' and '2' then '1 to 2' WHEN mag between '2' and '3' then '2 to 3' WHEN mag between '3' and '4' then '3 to 4' WHEN mag between '4' and '5' then '4 to 5' ELSE '10+' END AS mag from QUAKES1 WHERE net =  '" + str(range1) + "' and mag between '" + str(range2) + "' and '" + str(range3) + "' ) T  GROUP BY T.mag"

    cursor.execute(success)

    result_set = cursor.fetchall()
    state=[]
    print(result_set)
    for row in result_set:
        state.append(row[0])
        state.append(row[1])

    return render_template('index.html', ci=state)

@app.route("/bar2", methods=["POST", "GET"])
def bar2():
    range1 = str(request.form.get('range1', ''))
    range2 = int(request.form.get('range2', ''))
    range3 = int(request.form.get('range3', ''))
    # query1 = "SELECT StateName, Registered  FROM voting_i WHERE Voted BETWEEN 1 and 9000 "
    # query1 = "SELECT StateName ,count(Registered) AS number FROM voting_i GROUP BY StateName"

    # query1 = "SELECT Registered ,count(Registered) AS number FROM (SELECT CASE when Registered BETWEEN 0 and 9000 then 10000 WHEN Registered between 10000 and 19000 then 20000 WHEN Registered between 20000 and 29000 then 30000 ELSE 100 END AS Registered from voting_i) T  GROUP BY T.Registered"

    # query1 = "SELECT  latitude , count(latitude) AS number from (SELECT CASE when latitude BETWEEN '10' and '20' then '10 to 20' WHEN latitude between '20' and '30' then '20 to 30' WHEN latitude between '30' and '40' then '30 to 40' WHEN latitude between '40' and '50' then '40 to 50' ELSE '50+' END AS latitude from QUAKES1) T  GROUP BY T.latitude"
    query1 = "SELECT  mag, count(mag) AS number  from (SELECT CASE when mag BETWEEN '0' and '1' then '0 to 1' WHEN mag between '1' and '2' then '1 to 2' WHEN mag between '2' and '3' then '2 to 3' WHEN mag between '3' and '4' then '3 to 4' WHEN mag between '4' and '5' then '4 to 5' ELSE '10+' END AS mag from QUAKES1 WHERE net =  '" + str(range1) + "' and mag between '" + str(range2) + "' and '" + str(range3) + "' ) T  GROUP BY T.mag"


    cursor.execute(query1)
    r1 = cursor.fetchall()
    rows = ([['head1', 'Number of Earthquakes']])
    for ele in r1:
        rows.append([ele[0],ele[1]])

    return render_template('bar_h.html', rows=rows)

@app.route("/showpie2", methods=["POST", "GET"])
def showpie2():
    range1 = str(request.form.get('range1', ''))
    range2 = int(request.form.get('range2', ''))
    range3 = int(request.form.get('range3', ''))
    # query1 = "SELECT Registered ,count(Registered) AS number FROM (SELECT CASE when Registered BETWEEN '0' and '9000' then '10000' WHEN Registered between '10000' and '19000' then '20000' WHEN Registered between '20000' and '29000' then '30000' ELSE '100' END AS Registered from voting_i) T  GROUP BY T.Registered"
    # query1 = "SELECT  latitude , count(latitude) AS number from (SELECT CASE when latitude BETWEEN '10' and '20' then '10 to 20' WHEN latitude between '20' and '30' then '20 to 30' WHEN latitude between '30' and '40' then '30 to 40' WHEN latitude between '40' and '50' then '40 to 50' ELSE '50+' END AS latitude from QUAKES1 where net ='" + str(net) + "') T  GROUP BY T.latitude"
    query1 = "SELECT  mag, count(mag) AS number  from (SELECT CASE when mag BETWEEN '0' and '1' then '0 to 1' WHEN mag between '1' and '2' then '1 to 2' WHEN mag between '2' and '3' then '2 to 3' WHEN mag between '3' and '4' then '3 to 4' WHEN mag between '4' and '5' then '4 to 5' ELSE '10+' END AS mag from QUAKES1 WHERE net =  '" + str(range1) + "' and mag between '" + str(range2) + "' and '" + str(range3) + "' ) T  GROUP BY T.mag"

    cursor.execute(query1)
    r1 = cursor.fetchall()
    rows = ([['head1', 'head2']])
    for ele in r1:
        rows.append([ele[0],ele[1]])

    return render_template('showpie.html', rows=rows)

@app.route("/showpie1", methods=["POST", "GET"])
def showpie1():
    # query1 = "SELECT Registered ,count(Registered) AS number FROM (SELECT CASE when Registered BETWEEN '0' and '9000' then '10000' WHEN Registered between '10000' and '19000' then '20000' WHEN Registered between '20000' and '29000' then '30000' ELSE '100' END AS Registered from voting_i) T  GROUP BY T.Registered"
    query1 = "SELECT  latitude , count(*) AS number from (SELECT CASE when latitude BETWEEN '10' and '20' then '10 to 20' WHEN latitude between '20' and '30' then '20 to 30' WHEN latitude between '30' and '40' then '30 to 40' WHEN latitude between '40' and '50' then '40 to 50' ELSE '50+' END AS latitude from QUAKES1) T  GROUP BY T.latitude"
    cursor.execute(query1)
    r1 = cursor.fetchall()
    rows = ([['head1', 'head2']])
    for ele in r1:
        rows.append([ele[0],ele[1]])

    return render_template('showpie.html', rows=rows)






@app.route("/bar", methods=["POST", "GET"])
def bar():
    net = str(request.form.get('net', ''))
    # query1 = "SELECT StateName, Registered  FROM voting_i WHERE Voted BETWEEN 1 and 9000 "
    # query1 = "SELECT StateName ,count(Registered) AS number FROM voting_i GROUP BY StateName"

    # query1 = "SELECT Registered ,count(Registered) AS number FROM (SELECT CASE when Registered BETWEEN 0 and 9000 then 10000 WHEN Registered between 10000 and 19000 then 20000 WHEN Registered between 20000 and 29000 then 30000 ELSE 100 END AS Registered from voting_i) T  GROUP BY T.Registered"

    query1 = "SELECT  latitude , count(latitude) AS number from (SELECT CASE when latitude BETWEEN '10' and '20' then '10 to 20' WHEN latitude between '20' and '30' then '20 to 30' WHEN latitude between '30' and '40' then '30 to 40' WHEN latitude between '40' and '50' then '40 to 50' ELSE '50+' END AS latitude from QUAKES1 where net ='" + str(net) + "') T  GROUP BY T.latitude"

    cursor.execute(query1)
    r1 = cursor.fetchall()
    rows = ([['head1', 'Number of Earthquakes']])
    for ele in r1:
        rows.append([ele[0],ele[1]])

    return render_template('bar_h.html', rows=rows)


@app.route("/scatter1", methods=["POST", "GET"])
def scatter1():

    range1 = str(request.form.get('range1', ''))
    range2 = int(request.form.get('range2', ''))
    range3 = int(request.form.get('range3', ''))
    # query1 = "SELECT  latitude , count(latitude) AS number from (SELECT CASE when latitude BETWEEN '10' and '20' then '10 to 20' WHEN latitude between '20' and '30' then '20 to 30' WHEN latitude between '30' and '40' then '30 to 40' WHEN latitude between '40' and '50' then '40 to 50' ELSE '50+' END AS latitude from QUAKES1) T  GROUP BY T.latitude"

     # query1 = "SELECT nst, gap from [QUAKES1] where net='ci'"
    query1 = "SELECT nst, gap from QUAKES1 WHERE  net =  '" + str(range1) + "' and nst between '" + str(range2) + "' and '" + str(range3) + "'"
    # query1 = "SELECT nst, gap from QUAKES1 WHERE  net =  '" + str(range1) + "'"
    cursor.execute(query1)
    r1 = cursor.fetchall()
    rows1 = ([['MagnitudeType','nst']])
    # rows1 = ([['head1', 'Number of Earthquakes']])
    for val in r1:
        rows1.append([val[0],val[1]])
    return render_template('scatter.html', rows=rows1)



@app.route("/list", methods=["POST", "GET"])
def list():
    # depthrange1 = float(request.form.get('depthrange1', ''))
    # query1="SELECT * FROM earthq WHERE latitude >= '" + str(latitude1) + "' AND latitude <= '" + str(latitude2) + "' AND longitude >= '" + str(longitude1) + "' AND longitude <= '" + str(longitude2) + "'"


    # query1 = "select TIME,LATITUDE,LONGITUDE from QUAKES where NST between 2 and 3"
    query1 = "select * from voting_i where TotalPop between 2000 and 8000"
    cursor.execute(query1)
    r1 = cursor.fetchall()

    # query2 = "select TIME,LATITUDE,LONGITUDE from QUAKES where NST between 3 and 3"
    query2 = "select * from voting_i where TotalPop between 8000 and 40000"
    cursor.execute(query2)
    r2 = cursor.fetchall()

    return render_template('list.html', rows1=r1, rows2=r2)

# horizontal bar graph show number on each digit generated
@app.route("/bar1", methods=["POST", "GET"])
def bar1():
    r1 = []
    range1 = int(request.form.get('range1', ''))
    range1 = range1 + 1
    for i in range(1, range1):
        modulo = (i ** 3) % 10
        r1.append(modulo)

    r2 = []

    for i in range(range1 - 1):
        count = r1.count(r1[i])
        r2.append(count)

    rows = []
    rows.append(['Range Value', 'Number of Times'])

    for i in range(range1 - 1):
        rows.append([r1[i], r2[i]])

    return render_template('bar1.html', rows=rows)

@app.route("/scatter", methods=["POST", "GET"])
def scatter():
    range1 = int(request.form.get('range1', ''))
    range2 = int(request.form.get('range2', ''))

    # query1 = "SELECT count(LOCATIONSOURCE) FROM QUAKES WHERE MAG between '" + str(range1) + "' AND '" + str(range2) + "'"

    query1 = "SELECT count(StateName) FROM voting_i WHERE TotalPop/1000 between '" + str(
        range1) + "' AND '" + str(range2) + "'"
    cursor.execute(query1)
    r1 = cursor.fetchall()


    rows = ([
        # ['Mag', 'locationSource'],
        ['Population', 'State'],
        [str(range1) + '-' + str(range2), r1[0][0]]
    ])

    return render_template('scatter.html', rows=rows)


@app.route("/line", methods=["POST", "GET"])
def line():
    locationsrc = str(request.form.get('locationsrc', ''))
    range1 = float(request.form.get('range1', ''))
    range2 = float(request.form.get('range2', ''))
    range3 = float(request.form.get('range3', ''))
    range4 = float(request.form.get('range4', ''))
    range5 = float(request.form.get('range5', ''))
    range6 = float(request.form.get('range6', ''))

    query1 = "SELECT count(*) FROM QUAKES WHERE LOCATIONSOURCE = '" + str(locationsrc) + "' AND MAG between '" + str(
        range1) + "' AND '" + str(range2) + "'"
    cursor.execute(query1)
    r1 = cursor.fetchall()

    query2 = "SELECT count(*) FROM QUAKES WHERE LOCATIONSOURCE = '" + str(locationsrc) + "' AND MAG between '" + str(
        range3) + "' AND '" + str(range4) + "'"
    cursor.execute(query2)
    r2 = cursor.fetchall()

    query3 = "SELECT count(*) FROM QUAKES WHERE LOCATIONSOURCE = '" + str(locationsrc) + "' AND MAG between '" + str(
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

@app.route("/listveg", methods=["POST", "GET"])
def listveg():
    range1 = float(request.form.get('range1', ''))
    # range2 = float(request.form.get('range2', ''))

    return render_template('listveg.html', rows1=range1, rows3=range1 + 36)


@app.route("/listveg2", methods=["POST", "GET"])
def listveg2():
    range1 = str(request.form.get('range1', ''))

    query1 = "SELECT * FROM vegdata WHERE VEGTYPE = '" + str(range1) + "'"
    cursor.execute(query1)
    r1 = cursor.fetchall()

    return render_template('listveg2.html', rows1=r1)


@app.route("/showpieveg", methods=["POST", "GET"])
def showpieveg():
    veg_type = str(request.form.get('veg_type', ''))
    # query1 = "SELECT magType,NST FROM QUAKES WHERE LOCATIONSOURCE = 'ok'"
    query1 = "SELECT VEGITABLE ,QUANTITY  FROM vegdata1 WHERE VEGTYPE = '" + str(veg_type) + "'"
    cursor.execute(query1)
    r1 = cursor.fetchall()
    rows = ([['head1', 'head2']])
    for ele in r1:
        rows.append([ele[0],ele[1]])

    return render_template('showpie.html', rows=rows)

@app.route("/pie2", methods=["POST", "GET"])
def pie2():
    range1 = 'Broccoli'
    range2 = 'Cabbage'
    range3 = 'Coke'

    # query1 = "SELECT  sum(QUANTITY) FROM vegdata1 WHERE VEGTYPE = 'veg' GROUP BY VEGTYPE"
    query1 = "SELECT sum(QUANTITY) FROM vegdata1 WHERE VEGTYPE = 'veg' and VEGITABLE = 'Broccoli'"
    cursor.execute(query1)
    r1 = cursor.fetchall()

    query2 = "SELECT sum(QUANTITY) FROM vegdata1 WHERE VEGTYPE = 'veg' and VEGITABLE = 'Cabbage'"
    cursor.execute(query2)
    r2 = cursor.fetchall()

    query3 = "SELECT sum(QUANTITY) FROM vegdata1 WHERE VEGTYPE = 'veg' and VEGITABLE = 'Coke'"
    cursor.execute(query3)
    r3 = cursor.fetchall()

    rows1 = ([
        ['veg', 'Number'],
        [str(range1), r1[0][0]],
        [str(range2), r2[0][0]],
        [str(range3), r3[0][0]]

    ])
    range3 = 'Cheese'
    range4 = 'Bread'

    query4 = "SELECT sum(QUANTITY) FROM vegdata1 WHERE VEGTYPE = 'notveg' and VEGITABLE = 'Cheese'"
    cursor.execute(query4)
    r4 = cursor.fetchall()

    query5 = "SELECT sum(QUANTITY) FROM vegdata1 WHERE VEGTYPE = 'notveg' and VEGITABLE = 'Bread'"
    cursor.execute(query5)
    r5 = cursor.fetchall()

    rows2 = ([
        ['veg', 'Number'],
        [str(range3), r4[0][0]],
        [str(range4), r5[0][0]]
    ])

    return render_template('pie2.html', rows=[rows1, rows2])


# @app.route('/')
#
# @app.route('/index', methods=["POST", "GET"])
# def index():
#     # success="SELECT   Registered , count(Registered) AS number from (SELECT CASE when Registered BETWEEN 0 and 9000 then 10000 WHEN Registered between 10000 and 19000 then 20000 WHEN Registered between 20000 and 29000 then 30000 ELSE 100 END AS Registered from voting_i) T  GROUP BY T.Registered"
#     success = "SELECT   Registered , count(Registered) AS number from (SELECT CASE when Registered BETWEEN 0 and 9000 then 10000 WHEN Registered between 10000 and 19000 then 20000 WHEN Registered between 20000 and 29000 then 30000 ELSE 100 END AS Registered from voting_i) T  GROUP BY T.Registered"
#     cursor.execute(success)
#     result_set = cursor.fetchall()
#     state=[]
#     print(result_set)
#     for row in result_set:
#         state.append(row[0])
#         state.append(row[1])
#
#     return render_template('index.html', ci=state)



# @app.route('/index',methods=["POST", "GET"])
# def index():
#     cursor = conn.cursor()
#     success = "SELECT StateName FROM voting_i where TotalPop>=5000 and TotalPop<=10000"
#     success2 = "SELECT StateName from voting_i where TotalPop>10000 and TotalPop<=50000"
#     cursor.execute(success)
#     result_set = cursor.fetchall()
#     state = []
#     state2 = []
#     print(result_set)
#     for row in result_set:
#         state.append(row[0])
#         cursor.execute(success2)
#         result_set2 = cursor.fetchall()
#         for row in result_set2:
#             state2.append(row[0])
#
#         return render_template('index.html', ci=state, ci1=state2)



if __name__ == '__main__':
    app.debug = True
    app.run()

# port = os.getenv('PORT', '8080')
# if __name__ == '__main__':
#     app.debug = True
#     app.run(host='0.0.0.0', port=int(port))
