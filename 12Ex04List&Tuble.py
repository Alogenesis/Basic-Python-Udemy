''' First Excerise Get birthday to months show'''
birtyday = input('Please enter your birth day in the format DD-MM-YYYY: ')
print(birtyday)
months = ('January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December' )
index_month = int( birtyday[3:5])
var_index_month = index_month - 1
print('You were born in', months[var_index_month])

#Debug code
print(index_month)
print( type(index_month) )

'''
January
February
March
April
May
June
July
August
October
November
December
'''

'''2nd Excercise Add list'''
people = ['first','2nd','3rd']
name = input('Please enter your name: ')
people.append(name)
print(people)
