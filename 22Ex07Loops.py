import random

''' Ask 8 people name and random pick someone '''
people = []
while len(people) < 8 :
    person = input('Please Enter name : ')
    people.append(person)
print(people)
print(people[random.randint(0,4)])


''' Guess the color game '''

play_again = 'yes'
color = ['red', 'blue', 'green'] #'yellow', 'white', 'black', 'orange', 'purple', 'lightblue', 'gray'
while True:
    randomclue = random.randint(0,len(color)-1)
    print(randomclue)
    clue = color[randomclue]
    #print(clue)
    print("red / blue / green what color I'm thinking ? ")
    while True:
        guess = input('What your guess ? : ').lower()

        if guess == clue :
            print('Correct! You guessed it.')
            print("I'm thinking about", clue, "color")
            break
        else :
            print("Nope try again")

    print('Play again?')
    play_again = (input("Type 'no' for quit : ")).lower()
    if play_again == 'no':
        break

print("It's was fun. Thank for playing.")
