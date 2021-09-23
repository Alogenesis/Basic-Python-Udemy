'''
    Time and Pyplot
The game for type faster
'''
import time as t
import matplotlib.pyplot as plt

print("This program will help you type faster")
print("Type 'ok' 5 times")
input("Press enter to start")

times = []
mistake = 0
while len(times) < 5 :
    start = t.time() #เวลาเริ่ม
    word = input('>> ').lower()
    end = t.time()   #เวลาที่พิมพ์จบ
    if word != 'ok': #พิมพ์ผิดเวลาจะไม่บวก นับเฉพาะพิมพ์ถูก
        mistake += 1
        continue
    time_elapesed = end - start #เวลาที่ใช้ = เวลาที่พิมพ์จบ - เวลาเริ่ม
    times.append(time_elapesed)


print("You made",mistake,"mistake(s).")
print('Time Spend')
print(times)

'''matplotlib'''
x = [1,2,3,4,5]  #กำหนดค่าแกน x จากซ้ายไปขวา
y = times        #กำหนดค่าแกน y จากล่างขึ้นบน
plt.plot(x,y)
legend = ['1st','2nd','3rd','4th','5th'] #ตั้งชื่อให้แกน x ตัวที่ 1 2 3 4 5 จากซ้ายไปขวา
plt.xticks(x,legend)
plt.ylabel("Time spend in seconds")
plt.xlabel('Attemps')
plt.title('Typing Evolution')
plt.show()