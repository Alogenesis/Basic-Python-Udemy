''' install
1. terminal or cmd
2. pip install requests'''

'''send get request'''
import requests
r = requests.get("https://www.google.com") #Send get requst to google.com
print(r.status_code)  #check status
''' 
200 is ok
403 is forbidden mean something can't send and get
404 is Not found
'''

#print something from web
print(r.headers)
#Specific it
print(r.headers['Date'])

print("-------------------")

#look text
print(r.text)


