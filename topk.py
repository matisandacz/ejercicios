from heapq import heappop, heappush

"""



"""


def top(arr, k): # O(n log(k))



"""
def top(arr, k):
	if k >= len(arr):
		return arr

	# Armo un min heap con los primeros k elementos de arr
	h = []
	for i in range(k):  # O(k log(k))
		heappush(h, arr[i])

	# O (n log k)
	for i in range(k, len(arr)):
		if arr[i] > h[0]:
			heappop(h)
			heappush(h, arr[i])

	return h

arr = [1,2,3,6,1,2,26,6,5,19,2,1,3,5,7,20,21,22,34]
k = 5
print(top(arr, k))
"""