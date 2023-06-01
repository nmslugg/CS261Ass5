# Name: Nicholas Slugg
# OSU Email: sluggn@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 5
# Due Date: 05-31-22 (I used one late day)
# Description: This program implements a minimum heap using a dynamic array.


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
        """Adds a value to a heap"""
        self._heap.append(node)  # append node to array
        i = self._heap.length() - 1  # start at new value
        while i > 0:  # percolate value upwards
            if self._heap[(i-1)//2] > self._heap[i]:  # switch values if parent is less
                c = self._heap[(i-1)//2]
                self._heap[(i-1)//2] = self._heap[i]
                self._heap[i] = c
                i = (i-1)//2
            else:  # change to negative one to stop percolation
                i = -1

    def is_empty(self) -> bool:
        """Returns True if the heap is empty, False otherwise"""
        return self._heap.length() == 0  # true if the length of underlying array is zero

    def get_min(self) -> object:
        """Returns the minimum of a heap, raising exception if the heap is empty"""
        if self._heap.is_empty():  # raise exception if empty
            raise MinHeapException
        return self._heap[0]  # Minimum value is at head of heap

    def remove_min(self) -> object:
        """Removes the minimum value and restores heap structure, returning the value removed"""
        if self._heap.length() == 0:
            raise MinHeapException  # raises exception if it is empty
        r = self._heap[0]  # stores value to be returned
        self._heap[0] = self._heap[self._heap.length()-1]  # switches with end of array
        self._heap.remove_at_index(self._heap.length()-1)  # removes value at end
        _percolate_down(self._heap, 0)  # percolates top value down
        return r  # returns stored value

    def build_heap(self, da: DynamicArray) -> None:
        """Builds a heap from a provided dynamic array"""
        self._heap = DynamicArray()  # stores new dynamic array
        for item in da:
            self._heap.append(item)  # iterates through array adding value
        for i in range(self._heap.length()//2 - 1, -1, -1):
            _percolate_down(self._heap, i)  # percolates values of heap down for each non leaf value

    def size(self) -> int:
        """Returns the length of a heap"""
        return self._heap.length()  # returns length

    def clear(self) -> None:
        """Clears contents of heap"""
        self._heap = DynamicArray()  # change heap to empty dynamic array


def heapsort(da: DynamicArray) -> None:
    """Sorts contents of array into nonascending order using heapsort algorithm"""
    for i in range(da.length() // 2 - 1, -1, -1):
        _percolate_down(da, i)  # percolates each non leaf value to attain heap structure

    for i in range(da.length()-1, -1, -1):
        c = da[0]  # stores end of array
        da[0] = da[i]  # swaps end with front
        da[i] = c
        _percolate_down(da, 0, i-1)  # percolates front down, up to value replaced


def _percolate_down(da: DynamicArray, parent: int, maxdepth=None) -> None:
    """Percolates down a dynamic array in order to preserve heap structure"""
    if maxdepth is None:
        maxdepth = da.length()-1  # initialize max depth of array, this is initial value unless another is specified
    while parent >= 0:  # iterate through until heap structure is achieved
        l = 2*parent + 1  # store values for left and right of parent
        r = 2*parent + 2
        if l > maxdepth:
            parent = -1  # case where there are no more children
        elif (r > maxdepth) and da[parent] > da[l]:  # case where there is one child and they need to be swapped
            c = da[l]  # swaps parent and child values
            da[l] = da[parent]
            da[parent] = c
            parent = l  # new parent value is left child
        elif (r <= maxdepth) and da[parent] > min(da[l], da[r]):  # two children, at least one needs to be swapped
            if da[l] == min(da[l], da[r]):  # if left is to be swapped
                c = da[l]  # swaps parent and left
                da[l] = da[parent]
                da[parent] = c
                parent = l  # changes parent to left child
            else:  # case where right is to be swapped
                c = da[r]  # swaps parent and right child
                da[r] = da[parent]
                da[parent] = c
                parent = r  # new parent is right child
        else:  # in all other cases, heap status is reached, and iteration can be ended
            parent = -1

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

    print('\nPDF - build_heap example 2')
    print("--------------------------")
    da = DynamicArray(["hDuJWH_N", "fee", "g\e^ZrzGfs", "wYNH^sPqEi", "r[lryUwBb", "Kg", "'mTQO", "KAUZcw", "fee"])
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
