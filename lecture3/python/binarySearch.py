def binarySearch(A,key):
	n = len(A)
	if n == 1 and A[0] == key:
		return 0
	elif n == 1:
		return None
	
	if A[n/2] == key:
		return n/2
	elif key > A[n/2]:
		posInSubArray = binarySearch(A[n/2:], key)
		if not posInSubArray:
			return None
		else:
			return n/2 + posInSubarray
	else:
		return binarySearch(A[:n/2], key) #let potential None pass through


A = [1,2,3,4,5,6,7,8,9]
print binarySearch(A, 3)
print binarySearch(A, 10)
