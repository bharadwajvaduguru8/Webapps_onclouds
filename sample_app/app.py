#Python 3
from flask import *
import os


app = Flask(__name__)

print(os.getenv("PORT"))
port = int(os.getenv("PORT", 3000))

@app.route('/')
def question5():
    
     return render_template("start.html")
'''@app.route('/list', methods=['POST','GET'])
def list():
	conn = sqlite3.connect('database.db')
	cur = conn.cursor()
	#field=request.form['state']
	print(cur)
	#querry="Select * from people WHERE field3 =  '"+field+"' "
	#cur.execute(querry)
	#rows = cur.fetchall()
	#print (repr(rows))
    # return 'Hello World! I am running on port ' + str(port)
    # d = data()
	#return render_template("list.html",rows = rows)'''

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=port)
