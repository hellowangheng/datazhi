import numpy as np
import math
import random
from time import time
import matplotlib.pyplot as plt

t0=time()
x1=0
x2=1
count=0
count_s=0
list_x=[]
list_y=[]
# 计算积分
for i in range (1,101):
    list_x.append(i*10)
print(list_x[0])
for j in (list_x):
    for i in range(0,j):
        x= random.uniform(-1, 1)
        y = random.uniform(0, 1)
        count=count+1
        if y<-(x*x)+1:
            count_s=count_s+1
        elif y==-(x*x)+1:
            x1=x1+1
    list_y.append((count_s+x1/2)/count*2)
print("time=",time()-t0)
print("S=",list_y[10])

#绘图时，我需要记录每次的N，每次的结果。
#100000000  1.33334194
print(len(list_y))
print(len(list_x))
#plt.xlim(-1,100000000)
#plt.ylim((0,1.4))

plt.rcParams['savefig.dpi'] = 300 #图片像素
plt.rcParams['figure.dpi'] = 300 #分辨率
plt.plot(list_x,list_y)
plt.hlines(y=1.33333,xmin=-1,xmax=max(list_x),colors = "c", linestyles = "dashed")
#plt.plot(y=1.333333)
plt.show()

#计算π
list_p=[]
list_p_x=[]
max_count = 100000000
first_count =10
rate = 2
count_s = 0
j=0
while first_count < max_count:
    print(first_count)
    while j < first_count:
        x = random.uniform(-1, 1)
        y = random.uniform(0, 1)
        if   x**2 + y**2 < 1:
            count_s = count_s + 1
        j = j + 1
    list_p_x.append(first_count)
    list_p.append(count_s/first_count*4)
    j=0
    count_s=0
    first_count =first_count * rate
print("count_s = ",count_s)
print("pai  = ", list_p)
print("pai x = ", list_p_x)

plt.xlim(0,first_count/2)
plt.ylim(3,3.3)
plt.plot(list_p_x,list_p)
plt.hlines(y=np.pi,xmin= first_count,xmax=list_p_x, colors = "c", linestyles = "dashed")

plt.show()
# plt.hlines(y=1.33333,xmin=-1,xmax=max(list_x),colors = "c", linestyles = "dashed")

#绘图时，我需要记录每次的N，每次的结果。
#100000000  1.33334194
# print(len(list_y))
# print(len(list_x))
# #plt.xlim(-1,100000000)
# #plt.ylim((0,1.4))
#
# plt.rcParams['savefig.dpi'] = 300 #图片像素
# plt.rcParams['figure.dpi'] = 300 #分辨率
# plt.plot(list_x,list_y)
# plt.hlines(y=1.33333,xmin=-1,xmax=max(list_x),colors = "c", linestyles = "dashed")


