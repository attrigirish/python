#Delete using prepared statement(s)

import MySQLdb

try:
    con=MySQLdb.connect('localhost','root','mysql','aptech')
except Exception as e:
    print("Connection cannot be established : " + str(e))
    exit()


try:
    id=int(input("Enter ID : "))
    stmt="delete from student where id=%s"
    parameters=(id,)

    cur=con.cursor()
    cur.execute(stmt,parameters)

    con.commit()
    print("Deleted Successfully")
except Exception as e:
    print("Query Failed : " + str(e))
finally:
    con.close()
