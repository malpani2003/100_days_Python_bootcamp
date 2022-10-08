import mysql.connector as sql

myconn=sql.connect(
    host="localhost",
    user="root",
    passwd="",
    database="pythonlearn"
)

print(myconn)
print(myconn.is_connected()) # To check if connection is made properly or not
mycursor=myconn.cursor()  # Creating cursor instance

mycursor.execute("select * from admin") # execute() help to run sql querry
print(mycursor)

# To Fetch data from mycursor you can use three fetch...() function-:
# 1. fetchall()  - fetch all data 
# 2. fetchmany(<n>) - fetch n number of row 
# 3. fetchone() - fetch one data at a time 

data=mycursor.fetchall()  # to get data from result set

count=mycursor.rowcount   # rowcount will number rows in resultset
print(count)
print(data)

myconn.close() # After performing all tasks you need to stop the connection