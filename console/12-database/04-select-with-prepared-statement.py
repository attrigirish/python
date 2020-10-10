#Select using Prepared Statement

import MySQLdb

try:
    con=MySQLdb.connect('localhost','root','mysql','aptech')
except Exception as e:
    print("Connection cannot be established : " + str(e))
    exit()

try:
    stmt="select * from student"

    cur=con.cursor()
    cur.execute(stmt)

    #For Single Record
    #record=cur.fetchone()
    #print(record)

    #For All Records
    records=cur.fetchall()
    #print(records)

    for record in records:
        print("ID : ", record[0])
        print("Name : ", record[1])
        print("Course : ", record[2])
        print("Fees : ", record[3])
        print()
except Exception as e:
    print("Query Failed : " + str(e))
finally:
    con.close()
