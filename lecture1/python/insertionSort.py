#sorts in place, but here I return the sorted array to maintain interface consistency with mergeSort
def insertionSort(A):
	ASorted = A[:]
	for ind,x in enumerate(ASorted):
		j = ind-1
		while j >= 0 and ASorted[j] > x:
			ASorted[j+1] = ASorted[j]
			j -= 1
		ASorted[j+1] = x
	return ASorted

arrayToSort = [4,6,2,8,5,6,1] 
print arrayToSort
sortedArray = insertionSort(arrayToSort)
print sortedArray

