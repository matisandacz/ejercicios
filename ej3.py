def binary(arr, target):
	if(len(arr) == 1):
		return arr[0] == target
	mid = len(arr) // 2
	if(arr[mid] == target):
		return True
	if(target < arr[mid]):
		return binary(arr[:mid])
	return binary(arr[mid+1:])
	
#mid = ((target – A[0]) * (len(arr) - 1) / (A[len(arr) - 1] – A[0]));
