import random
from unicodedata import name

#print("first i ask if to click 1 for start")
beggin = str(input("welcom in just price, enter 1 for start: "))
# i print something for when i input "1"
print("you press " + beggin + "so we can start")
#in this part i creat a random value and the player have to guess it
ran = random.randint(0, 10000)
value = input("write a number: ")
i = 0
while value != ran and i < 7:
	if value < ran: print("greatter")
	else: print("smallest")
	value = input("write a number: ")
	i = i + 1
i = str(i)
if i < 7: 
	print("you won in "+ i + " tour")
else : 
	print("game over")
