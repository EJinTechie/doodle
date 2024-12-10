import random as rd
import datetime as dt
def my_rand():
    lst=list(range(1,1000000))
    return rd.sample(lst,10)

print(my_rand())