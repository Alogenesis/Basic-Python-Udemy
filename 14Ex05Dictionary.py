person = {'name' : 'Thanos', 'gender' : 'Male', 'age' : 68 ,
          'address' : 'Death moon', 'phone' : '123-1231'}
key = input('Please enter KEY for searching : ').lower()
print(person.get(key,'invalid propertie'))

# .lower() สามารถ force ได้ตั้งแต่รับค่า หรือจะมา force ทีหลังก็ได้