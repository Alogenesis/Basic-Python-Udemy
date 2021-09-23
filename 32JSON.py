import requests
r = requests.get("https://opentdb.com/api.php?amount=1&category=12&difficulty=easy&type=multiple")
print(r.status_code)
print(r.text)
print(type(r.text))

import json
question = json.loads(r.text)
print(question)

''' pip install pprint 
for json understanding '''

import pprint
pprint.pprint(question)

#Select it withh index
print( question['results'][0]['category'] )
print( question['results'][0]['incorrect_answers'] )

#Json are string
#This is how to convert Python to Json
person = {'Name':'Json' , 'Age':30}
print(person)
print(type(person))
person_json = json.dumps(person)  #convert function
print(person_json)
print(type(person_json))