number1 = input('Please enter the first number')
number2 = input('Please enter the second number')
print(number1)
print(number2)
print(number1 + number2)
'''everything from input are string'''
print(type(number1))
print(type(number2))

'''Let's use string input to create personal info'''
first_name = 'Winai'
last_name = 'Python'
print('My email address is', first_name + '.' + last_name + '@gmail.com')
'''force input'''
print(float(number1) + float(number2))
print(type(float(number1) + float(number2)))

'''Complete Program'''
print('------Start Program------')
print('This program calculate the average of two number.')
number1 = input('Please enter the first number')
number2 = input('Please enter the second number')
print('The number are', number1 ,'and', number2)
print('The average is: ', (float(number1) + float(number2)) / 2)
