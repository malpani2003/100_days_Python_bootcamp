student_score={
    "Harry":81,
    "Pranav":99,
    "Jhon":78,
    "SRK":74,
    "Tiger":10
}
print(student_score)

student_grade={}  # creating an empty dictionary

for key in student_score:
    score=student_score[key]
    if(score>=91 and score<=100):
        grade="Outstanding"
    elif(score>=81 and score<=90):
        grade="Exceeds Exellence"
    elif(score>=71 and score<=80):
        grade="Acceptable"
    elif(score<=70):
        grade="Fail"
    student_grade[key]=grade

print(student_grade)