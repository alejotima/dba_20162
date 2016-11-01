import cx_Oracle
conn = cx_Oracle.connect('sys', '12345678', 'localhost:1521/orcl', mode = cx_Oracle.SYSDBA)
try:
    cur = conn.cursor()
    try:
        statement = 'CREATE USER c##test4 IDENTIFIED BY 12345'
        cur.execute(statement)
        conn.commit()
    finally:
        cur.close()
finally:
    conn.close()