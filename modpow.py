def modpow(a, n , m):
	# Submit the one that runs faster: top or bottom

	#
	"""
	#
	mtwo = m
	if n < 0:
		n = n * (-1)
		# a = a inv mod m
		mod = m
		x,y = 1,0
		if(mod == 1):
			return None
		while a > 1:
			q = a//mod
			t = mod
			mod = a%mod
			a = t
			t = y
			y = x-(q*y)
			x = t
		if x < 0:
			x = x+mod
		a = x
		#print("a: " + str(a))
		# a = a inv mod m

	w = a
	z = 1
	while n > 0:
		if n%2 == 1:
			z = (z*w)%mtwo
		w = (w**2)%mtwo
		n = n//2
	return z
	#
	"""
	#
	h = a
	j = n
	res = 1
	while j>0:
		if(j%2 == 1):
			res = (res*h)%m
		h = (h**2)%m
		j = j//2
	return res
	#
	#"""
	#


print("Returns (a^n)mod m")
j = int(input("Enter a value for a: "))
k = int(input("Enter a value for n: "))
l = int(input("Enter a value for m: "))
print(modpow(j,k,l))

# print(((177**877)*583)%1373)




