data_valid = False

while data_valid == False:
    grade1 = float( input("Type the grade of the first test : "))
    if grade1 < 0 or grade1 > 10:
        print('Grand should be between 0 and 10')
    else:
        data_valid = True

data_valid = False
while data_valid == False:
    grade2 = float( input("Type the grade of the second test : "))
    if grade2 < 0 or grade2 > 10:
        print('Grand should be between 0 and 10')
    else:
        data_valid = True

data_valid = False
while data_valid == False:
    total_clase = float( input("Type the number of total class : "))
    if total_clase <= 0 :
        print('Total class can not be zero or less')
    else:
        data_valid = True

data_valid = False
while data_valid == False:
    absences = float( input("Type the number of absences class : "))
    if absences < 0 or absences > total_clase :
        print('Total class can not be zero or greater than total class')
    else:
        data_valid = True

#absences = int( input("Type the number of absences class : "))
#total_clase = int( input('Type the total number of class '))

avg_grade = (grade1 + grade2) / 2
attendance = (total_clase - absences) / total_clase

print('Average grade :', round(avg_grade,2))
print('Attendance rate :', str(round((attendance*100),2)))
if (avg_grade >= 6): #if grade pass
    if (attendance >= 0.8): #if attendance pass
        print("The student has been approved.")
    else : #if grade pass but fail attd
        print('The student has failed due to an attendance lower than 80%.')
elif (attendance >= 0.8): #if attd pass (but avg failed)
    print('The student has failed due to an average grade lower then 0.6 ')
else :
    print("The student has fail due to an average grade lower then 0.6 and attendance lower than 80%. ")