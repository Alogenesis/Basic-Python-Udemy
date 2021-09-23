data_valid = False

while data_valid == False:
    grade1 = input("Type the grade of the 1st test : ")
    try:
        grade1 = float(grade1)
        print('Grade1 =', grade1)
    except:
        print('Invalid input. Only number are accepted. Decimal should be seperate with a dot.')
        continue #continue meaning restart the loop

    if grade1 < 0 or grade1 > 10:
        print('Grand should be between 0 and 10')
    else:
        data_valid = True

data_valid = False

while data_valid == False:
    while True:
        grade2 = input("Type the grade of the 2nd test : ")
        try:
            grade2 = float(grade2)
            print('Grade2 =', grade2)
            break
        except:
            print('Invalid input. Only number are accepted. Decimal should be seperate with a dot.')
    if grade2 < 0 or grade2 > 10:
        print('Grand should be between 0 and 10')
    else:
        data_valid = True


data_valid = False

while data_valid == False:
    while True:
        total_clase = input("Type the number of total class : ")
        try:
            total_clase = int(total_clase)
            print('Total classs =', total_clase)
            break
        except:
            print('Invalid input. Only integer number are accepted.')
    if total_clase <= 0:
        print('Total class can not be zero or less')
    else:
        data_valid = True


data_valid = False

while data_valid == False:
    while True:
        absences = input("Type the number of absences class : ")
        try:
            absences = int(absences)
            print('absences =', absences)
            break
        except:
            print('Invalid input. Only integer number are accepted.')
    if absences < 0 or absences > total_clase:
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

