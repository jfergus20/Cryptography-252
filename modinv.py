def modinv(a,m):
	mod = m
	x,y = 1,0
	if(mod == 1):
		return None
	while a > 1:
		if m == 0:
			return x
		q = a//m
		b = m
		m = a%m
		a,b = b,y
		y = x-(q*y)
		x = b
	if x < 0:
		x = x+mod
	return x


j = int(input("Enter a value for a: "))
k = int(input("Enter a value for m: "))
print(modinv(j,k))