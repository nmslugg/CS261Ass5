# Name:
# OSU Email:
# Course: CS261 - Data Structures
# Assignment:
# Due Date:
# Description:


from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return 'HEAP ' + str(heap_data)

    def add(self, node: object) -> None:
        self._heap.append(node)
        i = self._heap.length() - 1
        while i > 0:
            if self._heap[(i-1)//2] > self._heap[i]:
                c = self._heap[(i-1)//2]
                self._heap[(i-1)//2] = self._heap[i]
                self._heap[i] = c
                i = (i-1)//2
            else:
                i = -2

    def is_empty(self) -> bool:
        return self._heap.length() == 0

    def get_min(self) -> object:
        return self._heap[0]

    def remove_min(self) -> object:
        if self._heap.length() == 0:
            raise MinHeapException
        r = self._heap[0]
        self._heap[0] = self._heap[self._heap.length()-1]
        self._heap.remove_at_index(self._heap.length()-1)
        cont = True
        parent = 0
        while cont:
            if self._heap.length() - 1 < max(2*parent + 1, 2*parent + 2):
                break
            if self._heap[parent] > self._heap[2*parent + 1]:
                _percolate_down(self._heap, parent)
                parent = 2*parent + 1
            elif self._heap[parent] > self._heap[2*parent + 2]:
                _percolate_down(self._heap, parent)
                parent = 2*parent + 2
            else:
                cont = False
        return r

    def build_heap(self, da: DynamicArray) -> None:
        self._heap = DynamicArray()
        for item in da:
            self._heap.append(item)
        print(self._heap.length()//2 - 1)
        for i in range(self._heap.length()//2 - 1, -1, -1):
            _percolate_down(self._heap, i)

    def size(self) -> int:
        return self._heap.length()

    def clear(self) -> None:
        self._heap = DynamicArray()


def heapsort(da: DynamicArray) -> None:
    """
    TODO: Write this implementation
    """
    pass


# It's highly recommended that you implement the following optional          #
# function for percolating elements down the MinHeap. You can call           #
# this from inside the MinHeap class. You may edit the function definition.  #

def _percolate_down(da: DynamicArray, parent: int) -> None:
    if da[parent] > min(da[2*parent + 1], da[2*parent+2]):
        if da[2*parent + 1] == min(da[2*parent + 1], da[2*parent+2]):
            c = da[2*parent + 1]
            da[2*parent + 1] = da[parent]
            da[parent] = c
        else:
            c = da[2*parent + 2]
            da[2 * parent + 2] = da[parent]
            da[parent] = c


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - is_empty example 1")
    print("-------------------")
    h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    print(h.is_empty())

    print("\nPDF - is_empty example 2")
    print("-------------------")
    h = MinHeap()
    print(h.is_empty())

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty() and h.is_empty() is not None:
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)

    print("--------------------------")
    print("Inserting 500 into input DA:")
    da[0] = 500
    print(da)

    print("Your MinHeap:")
    print(h)
    if h.get_min() == 500:
        print("Error: input array and heap's underlying DA reference same object in memory")

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())

    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())

    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)
