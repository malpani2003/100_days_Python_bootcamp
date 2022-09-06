student_score=input("Enter score of students: ")
student_score_list=student_score.split(",")
print(student_score_list)
lenght=len(student_score_list)
largest=int(student_score_list[0])
for score in student_score_list:
    if(int(score)>largest):
        largest=int(score)
print("Largest Score is: ",largest)
