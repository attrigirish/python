#Search using prepared statement(s)

import MySQLdb

try:
    con=MySQLdb.connect('localhost','root','mysql','aptech')
except Exception as e:
    print("Connection cannot be established : " + str(e))
    exit()


try:
    id=int(input("Enter ID : "))
    stmt="select * from student where id=%s"
    parameters=(id,)

    cur=con.cursor()
    cur.execute(stmt,parameters)

    record=cur.fetchone()

    print(record)
except Exception as e:
    print("Query Failed : " + str(e))
finally:
    con.close()
