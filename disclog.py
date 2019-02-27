def disclog(g,h,p):
	y = g
	for x in range(1,1000000000000000000000):
		if(y == h):
			return x
		y = (y*g)%p
	return -1


print("Returns x in g^x == h mod m")
j = int(input("Enter a value for g: "))
k = int(input("Enter a value for h: "))
l = int(input("Enter a value for p: "))
print(disclog(j,k,l))
