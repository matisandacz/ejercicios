def comparator(tuple1, tuple2):
    if (tuple1.value < tuple2.value):
        return tuple2
    return tuple1

def merge(arr_of_arr):
    A = min-heap()
    result = []
    for j in range(0, len(arrays)):
        heappush(A, (j, arrays[j][0], 0), comparator)
    while A.size() != 0:
        (index_array, value, index_inside_array) = extractMin(A)
        result.push(value)
        if index_inside_array+1 < len(arrays[index_array]):
            heappush(A, (index_array, arrays[index_array][index_inside_array+1], new_index), comparator)
    return result