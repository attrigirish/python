#Insert with User Input

import MySQLdb

try:
    con=MySQLdb.connect('localhost','root','mysql','aptech')
except Exception as e:
    print("Connection cannot be established : " + str(e))
    exit()

try:
    name=input("Enter Name : ")
    course=input("Enter Course : ")
    fees=float(input("Enter Fees : "))
    
    stmt="insert into student (name,course,fees) values('{}','{}',{})".format(name,course,fees)

    con.query(stmt)
    con.commit()
    print("Record Saved Successfully")
except Exception as e:
    print("Query Failed : " + str(e))
finally:
    con.close()
