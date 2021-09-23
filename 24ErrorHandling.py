''' If input aren't anything we expect we crash '''

number = input('Type a number : ') # if we input text, they crash

#use try and except
try:
    number = float(number)  #if input are float go on
    print("The number is :", number)
except: #if not float we send to this
    print("Invalid number")
