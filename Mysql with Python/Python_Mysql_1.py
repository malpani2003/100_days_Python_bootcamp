import mysql.connector as sql

myconn=sql.connect(
    host="localhost",
    user="root",
    passwd="",
    database="PythonLearn"
)

print(myconn)

