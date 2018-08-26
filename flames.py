# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 23:29:33 2018

@author: Raghul
"""

print(">>FLAMES<<")

a = input("Your Name: ")
b = input("Your Crush: ")

relation = {'f':a + " and " + b + " are friends.",\
            'l':a + " and " + b + " are in love.",\
            'a':b + " have affection on " + a + ".",\
            'm':b+" will marry "+a+".",\
            'e':b+" is an enemy of "+a+".",\
            's':b+" is a sister of "+a+"."}

a = list(a.lower().replace(" ",""))
b = list(b.lower().replace(" ",""))

result = list("flames")

count = 0

for i in range(len(b)):
    if b[i] in a:
        a[a.index(b[i])] = '*'
        b[i] = '-'
        count += 1

run = len(a) + len(b) - 2*count

newindex = 0

for i in range(6,1,-1):
    index = (newindex+run-1)%i
    result.remove(result[index])
    newindex = index%i

print(relation[result[0]])
