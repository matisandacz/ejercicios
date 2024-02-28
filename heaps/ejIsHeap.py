from heapq import heappop, heappush, heapify

# Determina si arr es un min heap O(n)
def is_heap(arr):
	for i in range(0, len(arr)//2):
		leftIdx = i*2+1
		rightIdx = i*2+2
		if leftIdx < len(arr) and arr[i] > arr[leftIdx]:
			return False
		if rightIdx < len(arr) and arr[i] > arr[rightIdx]:
				return False
	return True
	

arr = [10, 1, 2]
heapify(arr)
print(is_heap(arr))