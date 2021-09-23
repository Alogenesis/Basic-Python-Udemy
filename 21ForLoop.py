# For Loop are repeat every single thing in list[]
blog_post = ['The 10 Coolest math functions in Python',
             'How to make HTTP requests in Python',
             'A tutorial about data type in Python']

for post in blog_post:
    print(post)

sep = '-------------------------------'
print(sep)


# use continue to skip the step of the loop
blog_post = ['',
            'The 10 Coolest math functions in Python',
             '',
             'How to make HTTP requests in Python',
             'A tutorial about data type in Python']

for post in blog_post:
    print(post)

print(sep)

# using continue to skip '' blank
for post in blog_post:
    if post == '':
        continue
    print(post)
print(sep)

myString = 'This is my String'
for char in myString:
    print(char)
print(sep)

for x in range(0,10):
    print(x)
print(sep)

person = {'Name' : 'Karen Smith', 'Age': 25 , 'Gender' : 'female'} # 3 Element
for i in person:
    print(i, ':' , person[i]) #i just a variable and ':' just seperator text
print(sep)

#list in dict
blog_post = {'Python' : ['The 10 Coolest math functions in Python',
             'How to make HTTP requests in Python',
             'A tutorial about data type in Python'],
             'Javascript' : ['Namespace in Javasript', 'New function available']}
for catagory in blog_post:
    print('Post about', catagory)
    for post in blog_post[catagory]:
        print(post)
print(sep)