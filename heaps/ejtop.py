#!/bin/python3

import math
import os
import random
import re
import sys
import heapq
from typing import List, NamedTuple, Any, Optional, Tuple


class HeapElement(NamedTuple):
    """
    A heap element
    """
    priority: int
    element: Any

    def __lt__(self, other):
        return self.priority < other.priority

    def __le__(self, other):
        return self.priority <= other.priority

    def __eq__(self, other):
        return self.priority == other.priority

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        return self.priority > other.priority

    def __ge__(self, other):
        return self.priority >= other.priority


class MinHeap:
    """
    Heap of mins
    """
    def __init__(self, priorities: Optional[List[int]] = None,
                 elements: Optional[List[Any]] = None):
        """
        Creates a min heap

        :param priorities: an optional priority array to heapify
            for the initial status of the object
        :param elements: the elements associated with the priorities
            optional but must be given if priorities are given
        """
        self.array = []
        if priorities:
            if not elements:
                raise ValueError("The priorities need elements")
            self.array = [HeapElement(priority=p, element=e)
                          for p, e in zip(priorities, elements)]
        heapq.heapify(self.array)

    def push(self, priority: int, element: Any) -> None:
        """
        Pushes an element into the heap with the priority specified

        :param priority: the priority
        :param element: the element to push
        """
        elem = HeapElement(priority=priority,
                           element=element)
        heapq.heappush(self.array, elem)

    def pop(self) -> Tuple[int, Any]:
        """
        Pops the min out of the heap

        :return: a tuple with the priority and the element
        """
        min = heapq.heappop(self.array)
        return min.priority, min.element
    
    def top(self) -> Tuple[int, Any]:
        """
        Gets the top element
        :return: a tuple with the priority and the element
        """
        min = self.array[0]
        return min.priority, min.element


def top_k(nums, k):
    
    h = MinHeap()
    
    if k >= len(nums):
        return nums

    # Armo un min heap con los primeros k elementos de arr
    for i in range(k):  # O(k log(k))
        h.push(nums[i], nums[i])
        
    # O (n log k)
    for i in range(k, len(nums)):
        if nums[i] > (h.top()[1]):
            h.pop()
            h.push(nums[i], nums[i])

    # O (k log k)
    result = []
    for i in range(k):
        result.append(h.pop()[1]) 
    result.sort(reverse=True)
    return result
    
    
    
if __name__ == "__main__":
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nums = [int(x) for x in input().split(" ")]
    k = int(input())
    result = top_k(nums, k)

    fptr.write(' '.join(map(str, result)))

    fptr.close()
