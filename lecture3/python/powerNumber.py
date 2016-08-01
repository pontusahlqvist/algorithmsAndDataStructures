def powerNumber(x,n):
	if n == 1:
		return x
	tmp = powerNumber(x,n/2)
	
	if n%2 == 0:
		return tmp*tmp
	else:
		return x*tmp*tmp

print powerNumber(2,10)
print powerNumber(2,11)
