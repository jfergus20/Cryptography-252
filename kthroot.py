def kthroot(k,y,p):
	# assuming k is invertible
	# x^k = y mod p

	a = k
	m = p-1

	mod = m
	x,j = 1,0
	if(mod == 1):
		return None
	while a > 1:
		if m == 0:
			return x
		q = a//m
		b = m
		m = a%m
		a,b = b,j
		j = x-(q*j)
		x = b
	if x < 0:
		x = x+mod
	l = x

	#l = modinv(k,p-1)
	z = pow(y,l,p)
	w = pow(z,k,p)
	print("x: " + str(x))
	print("z: " + str(z))

	return z



print("Expected: 2")
print(kthroot(3,3,5))
print()
print("Expected: 11")
print(kthroot(13,7,41))
print()
print("Expected: 1810")
print(kthroot(2027,2273,2707))
print()
print("Expected: 4783942")
print(kthroot(9159071,11453170,12286471))