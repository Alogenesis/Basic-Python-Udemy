'''Kilometers to Miles converter'''
mile = 1.609344
km = input("Please enter a number of Kilometers")
print(km, "Kilometers are eqaul", ((float(km))/mile), "Miles")

'''Tips'''
'''1. Force input'''
km = float(input("Please enter a number of Kilometers"))
result = km / mile
print(km, "Kilometers are eqaul", result , "Miles")

'''2. Force decimal with round function'''
km = float(input("Please enter a number of Kilometers"))
result = km / mile
print(km, "Kilometers are eqaul", round(result,4) , "Miles")