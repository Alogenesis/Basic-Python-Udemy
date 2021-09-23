#install MatPlotLib
'''
1. Terminal or cmd
2. pip install matplotlib
'''

import matplotlib.pyplot as plt
x = [1,2,3,4] #x bar value
y = [1500,1200,1100,1800] #y bar value
plt.plot(x,y) #let's it plot
plt.show() #Show it
legend = ['Jan', 'Feb', 'Mar', 'Apr'] #Change name for y : legend just a var
plt.xticks(x,legend) #use x and legend to be x,y
plt.plot(x,y) #plot it
plt.show() #show it ... press x for clear first window for see

#another one
plt.bar(x,y) #Plot x,y
plt.ylabel("Sale in US$") # y bar name = sale in us

plt.title('Monthly Sale') # x bar name = monthly sale

plt.show() #show them