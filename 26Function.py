def say_hello():
    print("Hello!!")

say_hello()
say_hello()
say_hello()

def greeting(someVarible): #need 1 assigh in ()
    print("Hello "+  someVarible + " How are you doing?")

greeting('Mary Potter')

def greetingpeople(person1,person2): #need 2 assign in()
    print("Hello "+ person1 + " How are you? " + person2 + " are waiting for you.")
greetingpeople('Sarah','Fenrir')

def greetingpeople(person1,person2='The director'): #need 1 or 2 assign in() because second var was assigned
    print("Hello "+ person1 + " How are you? " + person2 + " are waiting for you.")
greetingpeople('Sarah')
greetingpeople('Sarah','Fen')


def fahr2celsius(fahr):
    clesius = (5* (fahr - 32)) / 9
    return clesius
print("Celsius are" ,fahr2celsius(100), 'degree')