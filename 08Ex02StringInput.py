fname = input('Please enter your first name')
mname = input('Please enter your middle name')
lname = input('Please enter your last name')
full_name = fname + ' ' + mname + ' ' + lname
print('"Your fullname are', full_name + '"')
print('"Your initials are', fname[0],mname[0],lname[0])
print('--------------------')

'''Product Lot number'''
number = "037-00901-00027"
'''Use index number'''
print('Country Code:',number[0:3])
print('Product Code:',number[4:9])
print('Batch Code:',number[-5:])

'''Split text'''
x,y,z = number.split("-")
print(x,y,z)
print('Country Code:',x)
print('Product Code:',y)
print('Batch Code:',z)

