def mountain(arr):

	if(len(arr) <= 2):
		return max(arr)

	mid = len(arr) // 2

	if(arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]):
		return arr[mid]

	if(arr[mid] > arr[mid-1]):
		 return mountain(arr[mid+1:])

	return mountain(arr[:mid])

print(mountain([1,2,3,4,5,6,8,7,6]))

def mountain(arr):
	low = 0
	high = len(arr) - 1

	if(high-low+1) <= 2:
		return max(arr)

	while(low <= high):
		mid = len(arr) // 2
		if(arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]):
			return arr[mid]

