# Heapify implemented with Sift-Down to creatte a Min-heap
def swap(A, i, j):
	tmp = A[i]
	A[i] = A[j]
	A[j] = tmp

def siftDown(A, i):
	leftIdx = 2*i+1
	rightIdx = 2*i+2

	smallestIdx = i

	if(leftIdx < len(A) and A[leftIdx] < A[smallestIdx]):
		smallestIdx = leftIdx

	if(rightIdx < len(A) and A[rightIdx] < A[smallestIdx]):
		smallestIdx = rightIdx

	if(smallestIdx != i):
		swap(A, i, smallestIdx)
		siftDown(A, smallestIdx)

def heapify(A):
	for i in range(len(A)//2, -1, -1):
		siftDown(A, i)

if __name__ == '__main__':
	A = [4,3,2,1]
	heapify(A)
	print(A)