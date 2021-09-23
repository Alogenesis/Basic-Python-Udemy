''' Create Read Write Append File
mode
w = over write
a = append
x = create new file


'''

#Read mode - none
#f = open("35TextFile.txt")      #assign
#print(f.read())                 #read f

''' Careful : don't forget to open file before go mode. '''
#Over write mode - "w"
f = open("35TextFile.txt",'w')
f.write("This file has been overwrote.")

f = open('35TextFile.txt')
print(f.read())

#Append Mode - "a"
f = open('35TextFile.txt', 'a')
f.write('\nThis text will append to text file')
f = open('35TextFile.txt')
print(f.read())

#Create Mode - "x"
f = open("35TextFileCreateByPython","x")

#Create on path(ex.desktop) mode - "x"
''' Not work code 
f = open("Users\User\Documents",'x')
'''