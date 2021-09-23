'''List (can edit)'''
student = 'John, Mary, Steve'
student = ['John', 'Mary', 'Steve']  #List อยู่ใน [ ]
print(type(student)) #List
print(len(student)) #3 จำนวนสมาชิกของ List
print(student[0])   #John index 0
print(student[-1])  #Steve Last student
print(student[0:2]) #John Mary  เอา 2 คนแรกไม่เอาคน 3


'''Tuble Can't be change'''
months = ('January', 'February', 'March', )
print(type(months)) #Tuble
print(months[0])    #January

'''Try to change value'''
#Change List
student[0] = 'New Student' #try to change value on first student
print(student[0]) #New Student
print(student)
student.append('Sara')  #Add Sara
print(student)
#Add Peter to be index 0
student.insert(0, 'Pete')
print(student)
#Pop = remove last member
student.pop() #Sara remove (last member)
print(student)
student.pop(1) #remove index 1 = new student remove
print(student)
student.remove('Mary') #specific remove Mary
print(student)

''' Merge List '''
student2 = ['Paul', 'Kloey']
print(student)
print(student2)
sum_student = student+student2
print(sum_student)


#Change Tuble
months[0] = 'New month' #ทำไม่ได้ ติด Error
print(months)
