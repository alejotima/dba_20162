from flask import Flask, render_template, jsonify
import cx_Oracle
import os

app= Flask(__name__, static_url_path='/static')

@app.route('/api/users', methods=["GET"])
def get_all_users():
	try:
		cur = conn.cursor()
		try:
			cur.execute('''SELECT id, name, lastname FROM usuario''')
			result = []
			for identificador, name, lastname in cur:
				result.append({'id': identificador,'name':name,'lastname': lastname})
			return jsonify(result)
		finally: cur.close()
	finally: 
		print 'fin get'





@app.route('/api/users', methods=["POST"])
def insert_user():
	return 'esto es un post'

@app.route ('/api/users/<int:id>', methods=["DELETE"])
def delete_user(id):
	return 'esto es un delete - '+str(id)

@app.route ('/')
def home():
	return render_template('index.html')


if __name__=="__main__":
	conn = cx_Oracle.connect('sys', '12345678', 'localhost:1521/orcl', mode = cx_Oracle.SYSDBA)
	os.environ['NLS_LANG']='.UTF8'
	#host="0.0.0.0" Para hacer que nuestro servidor sea visible, publico en la red privada
	#port=5000 puerto 5000
	app.run(debug=True,host="0.0.0.0", port=5000)