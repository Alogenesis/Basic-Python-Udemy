'''Check type of data'''
myString = 'Some text'
print(type(myString), myString)
myString = '33'
print(type(myString), myString)
myString = 'She said "meet me at 5"'
print(type(myString), myString)
'''show index of myString'''
print(myString[-2]) #Count backward
print(myString[-1]) #Count backward
print(myString[0])  #Start
print(myString[1])  #Count forward
print(myString[2])
'''Count index of myString'''
print(len(myString)) #23
myString = 'She'
print(len(myString)) #3

'''Index selection'''
x = 'PT3456789'
print(x[0])     #select 1st char = P
print(x[0:5])   #select index 0 to 5 but not include 5 = 0 - 4 = PT345
print(x[:5])    #before : are blank = 0 so Same meaning x[0:5] = x[:5]
print(x[-2])    #select backward 2 char = 8 (0 = P , -1 = 9) only 1 char
print(x[-5:])    #select backward 5 char to the end ( after : are blank)
print(x[-2:-1]) #select backward 2 char not include -1 char = only 8
print(x[-4:-1]) #select backward 4 char to -2 char = 6 7 8

'''Tips : str can not + with number'''
#print("hello" + 123) error
print('user' + str(22)) #run = user22
'''str can * with number'''
print('user' * 3)  #run = useruseruser


