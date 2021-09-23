'''Number'''
num1 = 5
num2 = 3
print(type(num1))    #run = Int
result = num1 / num2
print(result)        #run = 1.66667
print(type(result))  #run = float
''' Don't use comma ( , ) for seperate 1000
    Do 1234567.12345
    Don't 123,456.123   '''

'''What we can do with Number'''
print(num1 + num2) #8
print(num1 - num2) #2
print(num1 * num2) #15
print(num1 / num2) #1.6667
print(num1 % num2) # ม็อด หาเศษ เหลือเศษ 2
print(num1 % 2)    # ม็อด 2 เพื่อหาว่าเป็นเลขคู่หรือคี่
print(5**4)        # ยกกำลัง
print(((2+2)/3/4)) # ทำในวงเล็บก่อน
print(round(4.87765)) #5 ปัดเศษ เต็มจำนวนเพราะไม่ระบุว่าเอากี่ตำแหน่ง
print(round(4.87765,2)) #4.88 เอาทศ 2 ตำแหน่ง

''' Import math module'''
import math
print(math.factorial(5)) #120
print(math.ceil(2.2)) #3 ปัดขึ้นตลอด
print(math.floor(2.8)) #2 ปัดลงตลอด
''' ดูข้อมูลเพิ่มเติม search : python math module '''



