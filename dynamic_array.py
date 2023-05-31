# Name: Nicholas Slugg
# OSU Email: sluggn@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 2
# Due Date: 05-01-23
# Description: This program provides the class for an implementation of a Dynamic Array.


from static_array import StaticArray


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._size = 0
        self._capacity = 4
        self._data = StaticArray(self._capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self._size) + "/" + str(self._capacity) + ' ['
        out += ', '.join([str(self._data[_]) for _ in range(self._size)])
        return out + ']'

    def __iter__(self):
        """
        Create iterator for loop
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._index = 0
        return self

    def __next__(self):
        """
        Obtain next value and advance iterator
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        try:
            value = self[self._index]
        except DynamicArrayException:
            raise StopIteration

        self._index += 1
        return value

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        return self._data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        self._data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return the capacity of the array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    def print_da_variables(self) -> None:
        """
        Print information contained in the dynamic array.
        Used for testing purposes.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        print(f"Length: {self._size}, Capacity: {self._capacity}, {self._data}")

    # -----------------------------------------------------------------------

    def resize(self, new_capacity: int) -> None:
        """This method takes in an integer, and increases the capacity of the dynamic array to be that integer"""
        if new_capacity <= 0:  # new capacity must be a positive integer
            pass
        elif new_capacity < self._size:  # new capacity must not be smaller than size
            pass
        else:
            store = StaticArray(self._capacity)  # new static array to store previous data
            store_size = self._size
            for i in range(self._size):  # iterate through to store previous data
                store.set(i, self._data.get(i))
            self._capacity = new_capacity
            self._data = StaticArray(self._capacity)
            for i in range(store_size):  # iterate through store, and add to previous data
                self.set_at_index(i, store.get(i))

    def append(self, value: object) -> None:
        """This method appends a value passed to the function, placing it at the end of the array"""
        if self._size == self._capacity:  # resizes the array if the capacity is full
            self.resize(2*self._capacity)
        self._data[self._size] = value  # adds value to final item is array
        self._size += 1  # increase size of array

    def insert_at_index(self, index: int, value: object) -> None:
        """This function inserts a value at the index passed to it, and it shifts all elements following it one place"""
        if index < 0 or index > self._size:  # raises DynamicArrayException for invalid indices
            raise DynamicArrayException
        self.append(value)  # adds value to end of list, this will also resize array, and increase size
        for i in range(1, self._size-index):  # iterate through dynamic array and moves the new element to correct position
            self.set_at_index(self._size-i, self.get_at_index(self._size-i-1))  # shift previous element
            self.set_at_index(self._size-i-1, value)  # insert new value in place

    def remove_at_index(self, index: int) -> None:
        """This method removes an element from an index passed to it, and shifts elements. If the array contains less
        than one quarter of its capacity, the array will be resized to twice its size"""
        if index < 0 or index >= self._size:  # raises DynamicArrayException for invalid indices
            raise DynamicArrayException
        if (self._size < 0.25 * self._capacity) and self._capacity > 10:
            self.resize(max(2*self._size, 10))  # resize array to maximum of twice its size or 10
        self._data[index] = None  # change value at index to None
        for i in range(index, self._size-1):  # iterate through list, and shift all elements to the left
            temp = self.get_at_index(i+1)
            self.set_at_index(i+1, None)
            self.set_at_index(i, temp)
        self._size -= 1  # subtract one from the size of the array

    def slice(self, start_index: int, size: int) -> "DynamicArray":
        """This method returns a new array starting from start_index sequentially, up through the size of array."""
        if start_index < 0 or start_index >= self._size:  # raises DynamicArrayException for invalid indices
            raise DynamicArrayException
        elif size < 0:  # raises DynamicArrayException for invalid size
            raise DynamicArrayException
        elif self._size - start_index < size:  # raises DynamicArrayException for too few elements at end of array
            raise DynamicArrayException
        dyna = DynamicArray()  # intialize new dynamic array
        for i in range(start_index, start_index + size):  # iterate through array up to the size desired
            dyna.append(self.get_at_index(i))  # appending new value to preserve order
        return dyna

    def merge(self, second_da: "DynamicArray") -> None:
        """This function appends all values of a second array passed"""
        for item in second_da:  # iterate through second array, and appends each item
            self.append(item)

    def map(self, map_func) -> "DynamicArray":
        """This function returns a new array containing all of the items of the previous array but transformed by
        map_func"""
        dyna = DynamicArray()  # new dynamic array to be returned
        for item in self:  # iterate through array and append transformed value
            dyna.append(map_func(item))
        return dyna

    def filter(self, filter_func) -> "DynamicArray":
        """This function will return a new dynamic array removing all elements by filter_func"""
        dyna = DynamicArray()  # dynamic array to be returned
        for item in self:  # iterate through array and filter out items flagged by filter_func
            if filter_func(item):
                dyna.append(item)
        return dyna

    def reduce(self, reduce_func, initializer=None) -> object:
        """This function will apply the reduce_func sequentially to all items in the array, and return the value. If
        initializer is passed, it will start from initializer"""
        if initializer is not None:  # start from initializer if passed
            return_val = initializer
            start = 0
        else:  # if not passed, start with first value
            return_val = self._data[0]
            start = 1
        for i in range(start, self._size):  # iterate through list, and apply reduce function to it
            return_val = reduce_func(return_val, self.get_at_index(i))
        return return_val


def find_mode(arr: DynamicArray) -> (DynamicArray, int):
    """This function finds the mode of a dynamic array, and will return all values, if there are multiple with same
    mode"""
    return_arr = DynamicArray()  # initial array to be returned
    m = 1  # counter for same type of element
    max_m = 1  # counter for maximum amount

    for i in range(arr.length()-1):  # iterate through list to count how many times the mode appears
        if arr.get_at_index(i) == arr.get_at_index(i + 1):
            m += 1  # add one to count if two elements in sequence are same
        else:
            m = 1  # if different return to count of 1
        if m > max_m:
            max_m = m  # update maximum count if greater than old maximum

    p = 1  # new counter for counting how many times an element appears

    if max_m == 1:  # edge case: if all elements occur once, include first element, since it won't be counted otherwise
        return_arr.append(arr.get_at_index(0))

    for i in range(1, arr.length()):  # iterate through array, and append any values that appear the maximum amount of times
        if arr.get_at_index(i) == arr.get_at_index(i-1):
            p += 1  # increase count if element appears more than once
        else:
            p = 1  # return count to one if different
        if p == max_m:
            return_arr.append(arr.get_at_index(i))  # append value to end of array

    return (return_arr, max_m)

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()

    # print dynamic array's size, capacity and the contents
    # of the underlying static array (data)
    da.print_da_variables()
    da.resize(8)
    da.print_da_variables()
    da.resize(2)
    da.print_da_variables()
    da.resize(0)
    da.print_da_variables()

    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)

    print("\n# append - example 1")
    da = DynamicArray()
    da.print_da_variables()
    da.append(1)
    da.print_da_variables()
    print(da)

    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)

    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.length())
    print(da.get_capacity())

    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)

    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Cannot insert value", value, "at index", index)
    print(da)

    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)

    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.length(), da.get_capacity())
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)

    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.length(), da.get_capacity())
    [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 3 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 4 - remove 1 element
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 6 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 7 - remove 1 element
    print(da.length(), da.get_capacity())

    for i in range(14):
        print("Before remove_at_index(): ", da.length(), da.get_capacity(), end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.length(), da.get_capacity())

    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)

    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")

    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")

    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)

    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)

    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))

    print("\n# map example 2")


    def double(value):
        return value * 2


    def square(value):
        return value ** 2


    def cube(value):
        return value ** 3


    def plus_one(value):
        return value + 1


    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))

    print("\n# filter example 1")


    def filter_a(e):
        return e > 10


    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))

    print("\n# filter example 2")


    def is_long_word(word, length):
        return len(word) > length


    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))

    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: (x // 5 + y ** 2)))
    print(da.reduce(lambda x, y: (x + y ** 2), -1))

    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))

    print("\n# find_mode - example 1")
    test_cases = (
        [1, 1, 2, 3, 3, 4],
        [1, 2, 3, 4, 5],
        ["Apple", "Banana", "Banana", "Carrot", "Carrot",
         "Date", "Date", "Date", "Eggplant", "Eggplant", "Eggplant",
         "Fig", "Fig", "Grape"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}\n")

    case = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    da = DynamicArray()
    for x in range(len(case)):
        da.append(case[x])
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}")
