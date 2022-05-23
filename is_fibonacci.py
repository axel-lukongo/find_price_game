#i input a value
value = input("input your value: ")
#i inatialize 3 value
#i compare with the value input while im smaller

x = 0
y = 1
n = x + y

while n < value:
	print(n)
	x = y
	y = n
	n = x + y

if n == value:
	print("this value is in fibonacci")
else:
	print("this value is not in fibonacci")