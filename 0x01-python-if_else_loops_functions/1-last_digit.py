#!/usr/bin/python3
import random
number = random.randint(-10000,10000)
lastdig=abs(number)%10
if lastdig > 5:
     print("greater than 5")
elif lastdig == 0:
     print("0")
elif lastdig < 6 and lastdig > 0:
     print("less than 6 and not 0")
