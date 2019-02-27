a = input('Enter value for a: ')
b = input('Enter value for b: ')
a = int(a)
b = int(b)
c = input('Enter value for c: ')
d = input('Enter value for d: ')
c = int(c)
d = int(d)



ls = [a, b, c, d]
"""
while a >= 0 and b >= 0:
   
   c = b
   if b == 0:
       break
   b = a%b
   a = c

print("The answer is: " + str(a))
"""




def gcdList(ls):
	list = []
	for i in range(len(ls)):
		for j in range(1, len(les)):
			print("i: " + i + "j: " + j)
			list += gcd(ls[i], ls[j])
			print("list: " + list)





def gcd(a, b):
	while b != 0:
		print("gcd(" + str(a) + " , " + str(b) +") = ")
		c = a%b
		a = b
		b = c
	return a




gcdList(ls)