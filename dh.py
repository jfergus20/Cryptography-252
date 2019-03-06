######################
# Diffie-Hellman/Alice
# Given a prime number p, an element g ∈ Z/pZ, and Bob’s transmission B
# function should return a pair of two numbers A,S, where A is the number you transmit to Bob, and S is the shared secret
######################
import random
def dh(g,p,B):
	a = random.randint(1,2**256)

	return (pow(g,a,p), pow(B,a,p))
	
"""
# TEST CASES



b = 8592
print("dh:")
A,S,p = dh(34482,46307,31043)
print("A: " + str(A))
print("S: " + str(S))
print(pow(A,b,p))
print(S%p)

b = 844986
print("dh:")
A,S,p = dh(1554,871181,860932)
print("A: " + str(A))
print("S: " + str(S))
print(pow(A,b,p))
print(S%p)

b = 1320566583
print("dh:")
A,S,p = dh(899210055,3281208851,2171840367)
print("A: " + str(A))
print("S: " + str(S))
print(pow(A,b,p))
print(S%p)





print("a: " + str(a))
print("pow(gap): " + str(pow(g,a,p)))
print("pow(Bap): " + str(pow(B,a,p)))


"""
