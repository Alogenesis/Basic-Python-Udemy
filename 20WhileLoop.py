''' guess number game '''
#newbie code
number = 5
guess = int( input("I'm thinking about a number between 0 - 10 you guess? : "))

while True:
    if guess == number:
        break
    else:
        guess = int( input("Nope. Try again : "))
print('You guessed it. I was thinking about', number)

#expert use import random
import random
print("Let's try one more time")
number = random.randint(0,10) #rand int
guess = int( input("I'm thinking about a number between 0 - 10 you guess? : "))

while True:
    if guess == number:
        break
    else:
        guess = int( input("Nope. Try again : "))
print('You guessed it. I was thinking about', number)
print("You're Winner")


#More Easy program for While Loop
''' Add person info for 5 people '''

people = []
while len(people) < 5 :
    person = input("Enter a name : ")
    people.append(person)
print(people)