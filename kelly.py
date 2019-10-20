import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt

#定义赢8次，输2次，1是赢，0是输
win=["1","0", "1", "1", "1","1", "1", "0", "1", "1"]
print(len(win))
#赢得话获利100%，输的时候损失100%,90的仓位
x1=(1+0.9)*100
x2=x1*0.1#输
x3=x2*(1+0.9)
x4=x3*(1+0.9)
x5=x4*(1+0.9)
x6=x5*(1+0.9)
x7=x6*(1+0.9)
x8=x7*0.1
x9=x8*(1+0.9)
x10=x9*(1+0.9)
dat=[x1,x2,x3,x4,x5,x6,x7,x8,x9,x10]
#查看每次输赢后还剩多少
print("-----------------赌博10次后--------------------")

dt=pd.DataFrame({'win':win,'dat':dat})
print(dt)
#绘制折线图查看每次剩余金额

plt.plot(dat)
plt.show()

#修改下注资金比例
#新建函数,进行调整仓位，传入，输赢，本金，赌局数，赔率，金额
def position(win,bal,pos):
    #x=win[0]
    profit=[]
    i=len(win)
    for i in win:
        if i == '1':
            #每次获取上一次剩余的金额
            bal = bal * (1 + pos)
        else:
            bal = bal * (1 - pos)
        profit.append(bal)
    return profit
print("-----------------90% 60% 40% 20% 10% 持仓--------------------")
pos90=position(win,100,0.9)
pos60=position(win,100,0.6)
pos40=position(win,100,0.4)
pos20=position(win,100,0.2)
pos10=position(win,100,0.1)
print(pd.DataFrame({'pos90':pos90,
                   'pos60':pos60,
                   'pos40':pos40,
                   'pos20':pos20,
                   'pos10':pos10}))
dat=pd.DataFrame({'pos90':pos90,
                   'pos60':pos60,
                   'pos40':pos40,
                   'pos20':pos20,
                   'pos10':pos10})
plt.plot(dat)
plt.legend(dat.head())
plt.show()
print("-----------------凯利公式--------------------")
#凯利公式,胜率，赔率,赔率亏损比例，净盈利
def kelly(prob,b,loss=1):
    f=(b*prob-loss*(1-prob))/(loss*b)
    return f
print(kelly(0.8,2))
print(kelly(0.45,2))
print("-----------------输赢概率生成--------------------")
def win_funtion(rate):
    win=np.ones(100,dtype=int)#默认100个1
    fail=np.random.randint(0,99,int(100-rate*100))
    print(fail)
    for i in fail:
        win[i]=0
    return win;
print("-----------------凯利公式考虑赔率--------------------")

def position(win, bal, pos, b):
    #x=win[0]
    profit=[]
    for i in win:
        if i == '1':
            # 每次获取上一次剩余的金额
            bal = bal * pos * b+bal
        else:
             #bal = bal *(1 - pos)- bal * pos * b
             bal = bal * (1 - pos)
        profit.append(bal)
    return profit
pos90=position(win,10,0.9,2)
pos80=position(win,10,0.8,2)
pos70=position(win,10,0.7,2)
pos60=position(win,10,0.6,2)
pos40=position(win,10,0.4,2)
pos20=position(win,10,0.2,2)
pos10=position(win,10,0.1,2)
print(pd.DataFrame({'pos90':pos90,
                    'pos70':pos70,
                   'pos60':pos60,
                   'pos40':pos40,
                   'pos20':pos20}))
#b = 赔率，等于期望盈利 ÷可能亏损（也就是盈亏比）
print(np.ones(5,dtype=int)[1])
print(np.random.randint(0,99,3))
print(win_funtion(0.81))
# print(np.random.randint(0,99,int((1-0.9)*100)))
# print(len(np.random.randint(0,99,int((1-0.8)*100))))
# print((100-0.8*100),int((1-0.8)*100))