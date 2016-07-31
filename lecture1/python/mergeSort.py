def mergeSort(A):
	if len(A) == 1:
		return A
	n = len(A)
	ALeft  = mergeSort(A[:n/2])
	ARight = mergeSort(A[n/2:])
	nLeft  = len(ALeft)
	nRight = len(ARight)

	#merge the two arrays
	merged = []
	i = 0
	j = 0
	while i < nLeft and j < nRight:
		l = ALeft[i]
		r = ARight[j]
		if l < r:
			merged.append(l)
			i += 1
		else:
			merged.append(r)
			j += 1

	#fill in the rest of whatever array is still non-empty
	while i < nLeft:
		merged.append(ALeft[i])
		i += 1
	while j < nRight:
		merged.append(ARight[j])
		j += 1
	return merged


arrayToSort = [4,6,2,8,5,6,1] 
print arrayToSort
sortedArray = mergeSort(arrayToSort)	
print sortedArray
