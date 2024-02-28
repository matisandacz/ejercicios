def solution(n, *args):

	for element in args:
		queue.add(element)
		if(len(queue) == n):
			print(sum(queue)/n)
			queue.pop()