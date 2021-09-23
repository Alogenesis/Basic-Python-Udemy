'''
1. Excel sheet downloaded
2. pip install pandas
3. pip install xlrd
'''

import pandas as pd
file = pd.ExcelFile("D:\User Data\Documents\GitHub\Udemy Python\sales.xlsx")  #path
print(file.sheet_names) #อ่านชื่อ Sheet ทั้งหมด
