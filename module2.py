import module1 as m
import math
import datetime as d
import os
import pandas as pd
import numpy as np
import matplotlib

arr=np.array([10,20,30,40])
print(arr)

data=pd.DataFrame([[1, 89],[None, 70],[3,60]], columns=["roll_no", "marks"], index=['a','b','c'])
print(data)
print(data.describe())
print(data.dropna())
print(data.fillna('0'))
print(data["marks"].max())
ser=pd.Series([89,70,65])
print(ser)


'''m.greeting("john")
print(math.exp(0))
print(math.sqrt(25))
print(d.datetime.now())
print(d.date(2024,10,2).strftime("%B"))

print(os.getcwd())
#print(os.mkdir("newfolder"))
print(os.chdir("C:\\Users\\Acer\\PycharmProjects\\web2\\newfolder"))
print(os.getcwd())
print(os.chdir(".."))
print(os.getcwd())
print(os.rmdir("newfolder"))'''