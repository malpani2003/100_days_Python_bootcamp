student_height=input("Enter height of students: ")
student_height_list=student_height.split(",")
print(student_height_list)
lenght=len(student_height_list)

sum=0
for i in range(0,lenght):
    sum=sum+int(student_height_list[i])
average_height=round(sum/lenght)
print("The average height of student is: ",average_height)
