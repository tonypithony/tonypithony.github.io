# pip install bottle
# pip install bottle-sqlite

import sqlite3
from bottle import route, run, template

@route('/anomal/db')
def show_anomal():
	db = sqlite3.connect('base2.db')
	c = db.cursor()
	c.execute("SELECT name,typeMutation,thickness,nebula,root FROM MutationCornea")
	data = c.fetchall()
	c.close()
	output = template('bring_to_anomal', rows=data)
	return output

run(host='0.0.0.0', port=8080) #http://0.0.0.0:8080/anomal/db