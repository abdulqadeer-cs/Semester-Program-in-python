from os import remove

student_score=[70,65,77,68,80]
print(student_score)
student_score.append(85)
print(student_score)
student_score.remove(70)
print("remove 70 :",student_score)
print(" Total Score :",sum(student_score))
print(" average Score: ",sum(student_score)/5)
print(" High Score: ",max(student_score))
print(" Lower Score : ",min(student_score))


