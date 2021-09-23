''' Dictionarie are detail of Things '''
person = { 'first_name':'John', 'last_name':'Cena', 'birth_year':1980}
print(type(person))
print(person)  #Look for dict info

#Change dict info on person
person['birth_year'] = 1978
print(person)   #birth_year = 1978 now : show result

person['marital_status'] = 'Married'  #Add marital status and give info
print(person)

person['children'] = ['Nathalie', 'Ethan'] #Add children status and info
print(person)

#Add Anna to children
person['children'].append('Anna')
print(person)

#find something on dictionary
print(person.get('Age','invalid property')) #get age but if not found print 'invalid property'

#Assing or naming for Key
key = 'first_name'
print(person[key])
#or meaning for
print(person['first_name'])

#คำสั่งลบข้อมูลทั้งหมดใน person
person.clear()
print(person)