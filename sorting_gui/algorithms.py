def bubble_sort(arr):
    """Bubble sort generator that yields the next indices to be swapped"""
    # Start sorting using bubble sort technique
    for i in range(len(arr) - 1):

        # After this iteration max element will come at last
        for j in range(len(arr) - i - 1):

            # Starting element is greater than the next element
            if arr[j] > arr[j + 1]:
                yield j, j + 1


def selection_sort(arr):
    """Selection sort generator that yields the next indices to be swapped"""
    for i in range(len(arr)):
        min_idx = i

        # Find the minimum element in the remaining unsorted list
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the minimum element with the first element
        yield i, min_idx


def insertion_sort(arr):
    """Insertion sort generator that yields the next indices to be swapped"""
    # Traverse through 1 upwards
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Push the element down until it's not less than the next element
        while j >= 0 and key < arr[j]:
            yield j, j + 1
            j -= 1


# TODO: algorithm isn't working yet
def merge_sort(arr):
    def __merge_sort(arr):
        """Merge sort generator that yields the next indices to be swapped"""
        # Base case
        if len(arr) <= 1:
            return arr
        
        # Internal function
        def merge(first_half, second_half):
            arr = []
            while len(first_half) > 0 and len(second_half) > 0:
                if first_half[0] < second_half[0]:
                    arr.append(first_half[0])
                    first_half.pop(0)
                else:
                    arr.append(second_half[0])
                    second_half.pop(0)

            while len(first_half) > 0:
                arr.append(first_half[0])
                first_half.pop(0)

            while len(second_half) > 0:
                arr.append(second_half[0])
                second_half.pop(0)

            return arr
        
        # "Divide and conquer"
        first_half = yield from __merge_sort(arr[:(len(arr) // 2)])
        second_half = yield from __merge_sort(arr[(len(arr) // 2):])

        return merge(first_half, second_half)
    
    yield from __merge_sort(arr)


def heap_sort(arr):
    """Heap sort generator that yields the next indices to be swapped"""
    # Internal function
    def heapify(arr, n, i):
        largest = i
        l = 2*i + 1
        r = 2*i + 2
    
        # Check if the left child of the root exists and is greater than the root
        if l < n and arr[largest] < arr[l]:
            largest = l
    
        # Check if the right child of the root exists and is greater than the root
        if r < n and arr[largest] < arr[r]:
            largest = r
    
        # Change root if needed
        if largest != i:
            yield i, largest
    
            # Heapify the root
            yield from heapify(arr, n, largest)
    
    n = len(arr)
 
    # Build a maxheap
    for i in reversed(range(n//2)):
        yield from heapify(arr, n, i)
 
    # Extract the elements one by one
    for i in reversed(range(n)):
        yield 0, i
        yield from heapify(arr, i, 0)


def quick_sort(arr):
    """Quick sort generator that yields the next indices to be swapped"""
    # Internal function
    def __quick_sort(arr, low, high):
        # Nested internal function
        def partition(arr, low, high):
            pivot = arr[high]
            i = low

            for j in range(low, high):
                if arr[j] < pivot:
                    yield i, j
                    i = i + 1

            yield i, high
            return i

        # Sort until the indices cross
        if low < high:
            index = yield from partition(arr, low, high)
            yield from __quick_sort(arr, low, index - 1)
            yield from __quick_sort(arr, index + 1, high)
    
    yield from __quick_sort(arr, 0, len(arr) - 1)


def cocktail_sort(arr):
    """Cocktail sort generator that yields the next indices to be swapped"""
    swapped = True
    iterate_up = True
    start = 0
    end = len(arr) - 1

    # Traverse up and down the list, sorting until it's sorted
    while swapped:
        swapped = False

        if iterate_up:
            # Going up
            for i in range(start, end): 
                if arr[i] > arr[i + 1]: 
                    yield i, i + 1
                    swapped = True
            
            end -= 1  # Decrement the end index
        else: 
            # Going down
            for i in range(end - 1, start - 1, -1): 
                if arr[i] > arr[i + 1]: 
                    yield i, i + 1
                    swapped = True
            
            start += 1  # Increment the start index
        
        iterate_up = not iterate_up  # Go the other direction


def odd_even_sort(arr):
    """Odd-even sort generator that yields the next indices to be swapped"""
    size = len(arr)
    swapped = True

    # Continue until the list is sorted
    while swapped: 
        swapped = False

        # Odd indices
        for i in range(1, size - 1, 2): 
            if arr[i] > arr[i + 1]: 
                yield i, i + 1
                swapped = True
        
        # Even indices
        for i in range(0, size - 1, 2): 
            if arr[i] > arr[i + 1]: 
                yield i, i + 1
                swapped = True


def shell_sort(arr):
    gap = len(arr) // 2

    while gap > 0:
        i = 0
        j = gap

        while j < len(arr):
            if arr[i] > arr[j]:
                yield i, j

            i += 1
            j += 1

            k = i
            while k - gap > -1:
                if arr[k - gap] > arr[k]:
                    yield k, k - gap
                k -= 1

        gap //= 2


def gnome_sort(arr):
    """Gnome sort generator that yields the next indices to be swapped"""
    index = 0

    # Continue until the index surpasses the length of the list
    while index < len(arr):
        if index == 0:
            index += 1
        if arr[index] >= arr[index - 1]:
            index += 1
        else:
            yield index, index - 1
            index -= 1


def pancake_sort(arr):
    """Pancake sort generator that yields the next indices to be swapped"""
    # Internal function
    def flip(arr, i):
        start = 0

        while start < i:
            yield i, start
            start += 1
            i -= 1

    # Start from the complete array and one by one reduce current size by one
    for curr_size in reversed(range(1, len(arr))):
        # Find index of the maximum element in the list
        max_index = arr.index(max(arr[:curr_size]))

        # Move the maximum element to end of the array if it's not already at the end
        if max_index != curr_size - 1:
            # To move at the end, first move the maximum number to the beginning
            yield from flip(arr, max_index)

            # Now move the maximum number to the end by reversing the current array
            yield from flip(arr, curr_size)


def stooge_sort(arr):
    """Stooge sort generator that yields the next indices to be swapped"""
    # Internal function
    def __stooge_sort(arr, l, h):
        if l < h:
            # If the first element is smaller than the last, swap them
            if arr[l] > arr[h]:
                yield l, h

            # If there are more than 2 elements in the array
            if h - l + 1 > 2:
                t = (h - l + 1) // 3

                # Recursively sort first 2 / 3 elements
                yield from __stooge_sort(arr, l, (h - t))

                # Recursively sort last 2 / 3 elements
                yield from __stooge_sort(arr, l + t, (h))

                # Recursively sort first 2 / 3 elements again to confirm
                yield from __stooge_sort(arr, l, (h - t))

    yield from __stooge_sort(arr, 0, len(arr) - 1)
