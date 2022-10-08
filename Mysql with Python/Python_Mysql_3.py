import mysql.connector as sql

myconn=sql.connect(
    host="localhost",
    user="root",
    passwd="",
    database="pythonlearn"
)
# print(myconn)
print(myconn.is_connected()) # To check if connection is made properly or not
mycursor=myconn.cursor()  # Creating a cursor instance
# print(mycursor)

mycursor.execute("INSERT INTO `admin`(`userid`, `password`) VALUES (3,12345)") # execute() help to run sql querry

myconn.commit()  # To make chnages in database run commit() function

myconn.close()

