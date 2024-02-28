lowers = MinHeap() # Max heap
highers = MinHeap() # Min heap

def add(num):

    # Agrego elemento al heap correspondiente
    if(len(lowers) == 0 or num < lowers.top()[1]):
        lowers.push(-num, num)
    else:
        highers.push(num, num)
    
    biggerHeap = lowers if len(lowers) >= len(highers) else highers
    smallerHeap = lowers if len(lowers) < len(highers) else highers
    
    # Rebalancear los heaps
    if(len(biggerHeap) - len(smallerHeap) > 1):
        elem = biggerHeap.pop()
        smallerHeap.push(-elem[0], elem[1])
 
def get_median():

    biggerHeap = lowers if len(lowers) >= len(highers) else highers
    smallerHeap = lowers if len(lowers) < len(highers) else highers

    if len(biggerHeap) == len(smallerHeap):
        return (biggerHeap.top()[1] + smallerHeap.top()[1]) / 2
    else:
        return biggerHeap.top()[1]