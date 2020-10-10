#Update using prepared statement(s)

import MySQLdb

try:
    con=MySQLdb.connect('localhost','root','mysql','aptech')
except Exception as e:
    print("Connection cannot be established : " + str(e))
    exit()


try:
    id=int(input("Enter ID : "))
    course=input("Enter Course : ")
    stmt="update student set course=%s where id=%s"
    parameters=(course,id)

    cur=con.cursor()
    cur.execute(stmt,parameters)

    con.commit()
    print("Updated Successfully")
except Exception as e:
    print("Query Failed : " + str(e))
finally:
    con.close()
