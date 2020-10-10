#Basic Insert

import MySQLdb

try:
    #Step 1 : Create Database Connection
    con=MySQLdb.connect('localhost','root','mysql','aptech')
except:
    print("Connection cannot be established")
    exit()

try:
    #Step 2 : Define the Statement
    stmt="insert into student (name,course,fees) values('Tanishq','Python',16000)"

    #Step 3 : Execute the Query
    con.query(stmt)

    #Step 4 : Commit the changes
    con.commit()
    print("Record Saved Successfully")
except:
    print("Query Failed")
finally:
    #Step 5 : Close the connection
    con.close()
