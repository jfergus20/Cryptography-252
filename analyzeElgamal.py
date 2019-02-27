def analyzeElgamal(g,p,A,c11,c12,m1,c21,c22):


	i = c12
	
	#### modinv(i,p)#######
	mod = p
	x,y = 1,0
	if(mod == 1):
		return None
	while i > 1:
		if p == 0:
			return x
		q = i//p
		b = p
		p = i%p
		i,b = b,y
		y = x-(q*y)
		x = b
	if x < 0:
		x = x+mod
	
	cinv = x
	#############

	print("cinv: " + str(cinv))
	print("c22: " + str(c22))
	print("m1: " + str(m1))
	print("mod: " + str(mod))


	m2 = (cinv*m1*c22)%mod

	print("m2: " + str(m2))

	return m2


## Test Cases ##

print("Expected: 34")
print("This should be 34: " + str(analyzeElgamal(2,101,59,89,67,24,89,36)))
print()
print("Expected: 1679")
print("This should be 1679: " + str(analyzeElgamal(3,2753,1321,42,339,2446,42,621)))
print()
print("Expected: 10387")
print("This should be 10387: " + str(analyzeElgamal(5,38803,15862,7712,226,21841,7712,22189)))