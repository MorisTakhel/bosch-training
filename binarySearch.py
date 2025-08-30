def binarySearch (arr:list, key:int):

	low = 0
	high = len(arr) - 1

	while low <= high:
		mid = low + (high - low)//2

		if arr[mid] == key:
			return mid

		elif arr[mid[ < key:
			low = mid + 1

		elif arr[mid] > key:
			high = mid - 1

	return -1
