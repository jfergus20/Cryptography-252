#
"""
#
def uandv(a,b):
	if b == 0:
		return (a,1,0)
	print("Step 1: u,g,x,y = 1,a,0,b")
	u,g,x,y = 1,a,0,b

	while y != 0:
		print("y = " + str(y))

		r = g%y
		print("r = g%y || " + str(g) + " % " + str(y) + " = " + str(r))

		q = (g-r)/y
		print("q = (g-t)/y || (" + str(g) + "-" + str(t) + ")/" + str(y) + " = " + str(q))

		s = u-(q*x)
		print("s = u-qx || " + str(u) + "-(" + str(q) + "*" + str(x) + ")" + " = " + str(s))
		
		u,g = x,y
		x,y = s,r

		print ("u = " + str(u))
		print("bottom of loop")
			
	if y == 0:
		v = (g-(a*u))/b
		print("v = (g-au)/b || (" + str(g) + "-" + str(a) + str(u) + ")/" + str(b) + " = " + str(v))

		return (g,u,v)


x = int(input("Enter a value for a: "))
y = int(input("Enter a value for b: "))

g,u,v = uandv(x,y)
print()
print("gcd(" + str(x) + "," + str(y) + ")" + " = " + str(g) + " u = " + str(u) + " v = " + str(v))
print()

#
"""
#


def extEuclid(a,b):
	r0,u0,v0 = a,1,0
	r1,u1,v1 = b,0,1

	while r1 !=0:
		q = r0//r1
		r2 = r0-(q*r1)
		u2 = u0-(q*u1)
		v2 = v0-(q*v1)
		r0,u0,v0 = r1,u1,v1
		r1,u1,v1 = r2,u2,v2
	return (u0,v0)

j = int(input("Enter a value for a: "))
k = int(input("Enter a value for b: "))

u,v = extEuclid(j,k)
print()
print(" u = " + str(u) + " v = " + str(v))
print()






