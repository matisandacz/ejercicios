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
        
    def isEmpty(self) -> bool:
        return len(self.array) == 0
        
    def size(self) -> int:
        return len(self.array)

        
# La idea es usar un max heap para almacenar todos los elementos de la primer mitad
# Y usar un min heap para almacenar todos los elementos de la segunda mitad.
# De esa forma los topes de ambos heaps me van a servir para calcular la mediana.
# Si los dos heaps tienen la misma longitud, entonces promedio
# Sino, tomo el tope del heap mas grande y esa va a ser la mediana.

# Como no tenemos max heaps, vamos a usar un min heap para simularlo.
# Para esto, insertamos elems con propridades invirtiendo el signo.
# en lowers.

# lowers <= highers
# dif de longitud entre lowers y highers no puede diferir en mas de 1. (parejos)

# Cuando llega un nuevo elemento, me fijo a que heap mandarlo
# cumpliendo la primer condicion

# Ahora tenemos que ver si se cumple la segunda condicion.
# Para esto, 

# Tenemos que detectar cual es el heap mas grande (dif >1)
# popear un elemento de ahi
# pushearlo al mas chiquito.

# cuando pusheo tengo q tener cuidado con las proridades.

#tuplas priority, element.
# Siempre que hagamos un pop, podemos ver el elemento
# Cuiado con un push al max heap. prioridad -elemento.

lowers = MinHeap() # max heap
highers = MinHeap() # min heap

def add(num):
    #Agregar elemento nuevo
    if(lowers.isEmpty() or num < lowers.top()[1]):
        lowers.push(-num, num)
    else:
        highers.push(num, num)
        
    # Cual es el heap mas grande
    biggerHeap = lowers if lowers.size() > highers.size() else highers
    smallerHeap = lowers if lowers.size() < highers.size() else highers
    
    #Rebalancear los dos heaps
    if(biggerHeap.size() - smallerHeap.size() > 1):
        elem = biggerHeap.pop()
        smallerHeap.push(-elem[0], elem[1])
 
def get_median():
    biggerHeap = lowers if lowers.size() >= highers.size() else highers
    smallerHeap = lowers if lowers.size() < highers.size() else highers
        
    if biggerHeap.size() == smallerHeap.size():
        return (biggerHeap.top()[1] + smallerHeap.top()[1]) / 2
    else:
        return biggerHeap.top()[1]

if __name__ == "__main__":
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nums = [int(x) for x in input().split(" ")]
    medians = []
    for i in range(len(nums)):
        add(nums[i])
        if i >= 1:
            medians.append(get_median())

    fptr.write(' '.join(map(str, medians)))

    fptr.close()