def linearSearch (arr:list, key:int):
	for index, curr in enumerate(arr):
		if curr == key:
			return index

	return -1
