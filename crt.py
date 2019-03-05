################################
# CHINESE REMAINDER THEOREM
################################

def crt(a1,m1,a2,m2):
	a = m1
	m = m2
	
	####################
	# Inverse
	####################
	mod = m
	i,j = 1,0
	if(mod == 1):
		return None
	while a > 1:
		if m == 0:
			return x
		q = a//m
		b = m
		m = a%m
		a,b = b,j
		j = i-(q*j)
		i = b
	if i < 0:
		i = i+mod
	####################

	y = ((a2 - a1) * i) % m2

	x = a1 + (m1 * y)
	####################
	
	return x





print("This should be 31: ")
print(crt(1,5,9,11))

print("This should be 9: ")
print(crt(4,5,1,4))
