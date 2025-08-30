def selectionSort (arr:list):

	for i in range(len(arr)):

		minIndex = i

		for J in range(i+1, len(arr)):
			if arr[j] < arr[minIndex]:
				minIndex = j		#finding the minimum

		arr[i], arr[minIndex] = arr[minIndex], arr[i]		#swap with the current first pointer

	return arr
