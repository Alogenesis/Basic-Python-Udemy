import time as t
print(t.localtime())

time_now = t.localtime()
print("Transaction completed at", str(time_now.tm_hour)+"h"+str(time_now.tm_min)+"m")

#time stamp : computer use it.
print(t.time())

#convert to normal local time : 86,400 sec are 1 day
# first we have time stamp
time_now  = t.time()
delivery_time = time_now + (86400*7) #convert to local human time
print(t.localtime(delivery_time))

#delay for next line code
t.sleep(5) #sleep 5 sec
print('5 Sec pass')

