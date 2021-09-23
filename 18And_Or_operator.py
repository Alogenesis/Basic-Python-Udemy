'''
This program for check average grade and attendance on student
if  avg.grade are >= 6 are pass
and attendanve are >= 80% are pass
if failed 1 or 2 are " Failed "
'''

grade1 = float( input("Type the grade of the first test : "))
grade2 = float( input("Type the grade of the second test : "))
absences = int( input("Type the number of absences class : "))
total_clase = int( input('Type the total number of class '))

avg_grade = (grade1 + grade2) / 2
attendance = (total_clase - absences) / total_clase

print('Average grade :', round(avg_grade,2))
print('Attendance rate :', str(round((attendance*100),2)))
if (avg_grade >= 6 and attendance >= 0.8): #if both pass
    print("The student has been approved.")
elif (avg_grade < 6 and attendance < 0.8) : #if both fail
    print("The student has fail due to an average grade lower then 0.6 and attendance lower than 80%. ")

elif (attendance < 0.8):  # if attd pass (but avg failed)
    print('The student has failed due to an attendance lower than 80%.')
else:
    print('The student has failed due to an average grade lower then 0.6')