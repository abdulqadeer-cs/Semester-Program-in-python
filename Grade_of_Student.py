#Grade of Student
marks=int(input("Student Grade :"))
if(marks>=94):
    print("4 GPA")
elif(marks>=87 and marks<94):
    print("3.67 GPA")
elif(marks>=78 and marks<87):
    print("3 GPA")
elif(marks>=68 and marks<78):
    print("2.67 GPA")
elif(marks>=64 and marks<68):
    print("2.3 GPA")
else:
    print("FAil")