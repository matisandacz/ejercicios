def top_k(nums, k):
    
    h = MinHeap() #O(1)

    for i in range(len(nums)):  # O(n log(k))
        h.push(nums[i], nums[i])
        if(len(h) > k):
            h.pop()
    
    result = []
    while(len(h)): # O(k log k)
        result.append(h.pop()[1]) 
    
    result.sort(reverse=True) # O(k log k)
    return result