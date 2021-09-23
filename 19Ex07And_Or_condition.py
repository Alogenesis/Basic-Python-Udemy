''' BMI Calculator '''

weight = float( input('Enter your weight in Kilogram unit(ex : 70.2) : '))
height = float( input('Enter your height in Meter unit(ex : 1.75) : '))
bmi = weight / (height*height)

if (bmi <= 18.5):
    print('Underweight')
elif(bmi > 18.5 and bmi <= 24.9):
    print('Normal weight')
elif (bmi > 24.9 and bmi <= 29.9):
    print('Overweight')
else:
    print('Obesity')
print('Your BMI are', round(bmi,2))
