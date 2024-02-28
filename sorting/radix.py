def counting(arr):

	# m = cota superior.
	m = max(arr)

	# Inicializo un arreglo de m listas vacias
	l = []
	for i in range(m+1):
		l.append([])
	
	# Agrego cada elemento a la lista correspondiente
	for i in range(len(arr)):
		l[arr[i]].append(arr[i])

	# Junto todas las listas en el output
	output = []
	for i in range(m+1):
		output.extend(l[i])

	print(output)
	return output


counting([1,2,3,5,1,4,9,0,1,2])
