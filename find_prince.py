import random
from unicodedata import name

#print("welcom in just price")
beggin = str(input("welcom in just price, enter 1 for start: "))
# i print something for when i input "1"
print("so you press " + beggin + " we can start")
#in this part i make the just price
ran = random.randint(0, 10000)
value = input("write a number: ")
i = 0
while value != ran:
	if value < ran: print("greatter")
	else: print("smallest")
	value = input("write a number: ")
	i = i + 1
i = str(i)
print("you won in "+ i + " tour")
