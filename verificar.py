def verificar(array): # O(n)
    for i in range(len(array)):
        leftIdx = i*2+1
        rightIdx = i*2+2
        if leftIdx < len(array) and array[i] > array[leftIdx]:
            return False
        if rightIdx < len(array) and array[i] > array[rightIdx]:
            return False
    return True