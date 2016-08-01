import time
import sys

def fibRecursive(n):
	if n == 0 or n == 1:
		return 1
	else:
		return fibRecursive(n-1) + fibRecursive(n-2)

def fibMemoized(n):
	fibNumbers = [1,1]
	for i in range(n+1)[2:]:
		fibNumbers.append(fibNumbers[i-1] + fibNumbers[i-2])
	return fibNumbers[-1]

def matrixMult(A,B):
	a0 = A[0]
	a1 = A[1]
	a2 = A[2]
	a3 = A[3]
	b0 = B[0]
	b1 = B[1]
	b2 = B[2]
	b3 = B[3]
	return [a0*b0 + a1*b2, a0*b1 + a1*b3, a2*b0 + a3*b2, a2*b1 + a3*b3]

def powerMatrix(M,n):
	if n == 1:
		return M
	tmp = powerMatrix(M,n/2)
	if n%2 == 0:
		return matrixMult(tmp,tmp)
	else:
		return matrixMult(matrixMult(tmp,tmp),M)

def fibMatrix(n):
	M = [1,1,1,0]
	MPow = powerMatrix(M,n)
	return MPow[0]

testCase = 30
try:
	testCase = int(sys.argv[1])
except:
	pass

print "Computing fibonacci(%d) three different ways"%testCase

t_a = time.time()
fRec = fibRecursive(testCase)
t_b = time.time()
fMem = fibMemoized(testCase)
t_c = time.time()
fMat = fibMatrix(testCase)
t_d = time.time()

print "\n\nUsing The recursive method, we found the value %d in a time %f seconds"%(fRec, t_b-t_a)
print "Using The memoized method, we found the value %d in a time %f seconds"%(fMem, t_c-t_b)
print "Using The matrix multiplication method, we found the value %d in a time %f seconds"%(fMat, t_d-t_c)

print "\n\n** The memoized algorithm was %.1fx faster than the recursive one"%((t_b-t_a)/(t_c-t_b))
print "** The matrix multiplication algorithm was %.1fx faster than the memoized one"%((t_c-t_b)/(t_d-t_c))

