from flask import Flask, render_template, jsonify, request
import cx_Oracle
import os

app= Flask(__name__, static_url_path='/static')

@app.route('/api/users', methods=["GET"])
def get_all_users():
	try:
		cur = conn.cursor()
		try:
			cur.execute('''SELECT id, name, lastname FROM test1''')
			result = []
			for identificador, name, lastname in cur:
				result.append({'id': identificador,'name':name,'lastname': lastname})
			return jsonify(result)
		finally: cur.close()
	finally: 
		print 'fin get'





@app.route('/api/users', methods=["POST"])
def insert_user():
    try:
        cur = conn.cursor()
        try:
            data = request.json
            print data
            statement = 'insert into test1(name,lastname) values (:2,:3)'
            cur.execute(statement,(request.json['name'], request.json['lastname']))
            conn.commit()
            return jsonify(True)
        finally:
            cur.close()
    finally:
        print 'Se inserto'

@app.route ('/api/users/<int:id>', methods=["DELETE"])
def delete_user(id):
    try:
        cur = conn.cursor()
        try:
            statement = 'delete from test1 where id = :id'
            cur.execute(statement,{'id':id})
            conn.commit()
            return jsonify(True)
        finally:
            cur.close()
    finally:
        print 'Se borro'

@app.route ('/')
def home():
	return render_template('index.html')


if __name__=="__main__":
    conn = cx_Oracle.connect('C##HR','12345', 'localhost:1521/orcl')
	#conn = cx_Oracle.connect('sys', '12345678', 'localhost:1521/orcl', mode = cx_Oracle.SYSDBA)
    os.environ['NLS_LANG']='.UTF8'
	#host="0.0.0.0" Para hacer que nuestro servidor sea visible, publico en la red privada
	#port=5000 puerto 5000
    app.run(debug=True,host="0.0.0.0", port=5000)