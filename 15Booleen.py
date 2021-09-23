'''
Booleens value are True / False
Comparison
 >
 <
 ==
 !=
 >=
 <=
'''

num1 = 8
num2 = 4
print(num1 > num2) #True 8 > 4
print(num1 < num2) #False 8 !< 4
myBooleen = True
print(type(myBooleen))

''' If Else statement '''

num1 = float( input('Type the first number : ') )
num2 = float( input('Type the second number : ') )
print( num1,'>',num2,'?')

if (num1 > num2):
    print(num1, 'is greater than', num2)
elif (num1 == num2):
    print(num1,'is equal',num2)
else :
    print(num1, 'is less than', num2)

