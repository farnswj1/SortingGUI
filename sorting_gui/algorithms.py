def bubble_sort(arr):
    """Bubble sort generator that yields the next indices to be swapped"""
    # Start sorting using bubble sort technique
    for i in range(len(arr) - 1):

        # After this iteration max element will come at last
        for j in range(len(arr) - i - 1):

            # Starting element is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                yield


def selection_sort(arr):
    """Selection sort generator that yields the next indices to be swapped"""
    for i in range(len(arr)):
        min_idx = i

        # Find the minimum element in the remaining unsorted list
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        yield


def insertion_sort(arr):
    """Insertion sort generator that yields the next indices to be swapped"""
    # Traverse through 1 upwards
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Push the element down until it's not less than the next element
        while j >= 0 and key < arr[j]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            yield
            j -= 1


def merge_sort(arr):
    """Merge sort generator that yields the next indices to be swapped"""
    # Internal function
    def __merge(arr, left, middle, right):
        for i in range(middle, right + 1):
            key = arr[i]
            j = i - 1

            # Push the element down until it's not less than the next element
            while j >= left and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
            yield

    def __merge_sort(arr, left, right):
        # Continue until the left index is not less than the right index
        if left < right:
            # "Divide and conquer"
            middle = (left + right) // 2
            yield from __merge_sort(arr, left, middle)
            yield from __merge_sort(arr, middle + 1, right)
            yield from __merge(arr, left, middle, right)
    
    yield from __merge_sort(arr, 0, len(arr) - 1)


def heap_sort(arr):
    """Heap sort generator that yields the next indices to be swapped"""
    # Internal function
    def __heapify(arr, n, i):
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
            arr[i], arr[largest] = arr[largest], arr[i]
            yield

            # Heapify the root
            yield from __heapify(arr, n, largest)
    
    n = len(arr)
 
    # Build a maxheap
    for i in reversed(range(n//2)):
        yield from __heapify(arr, n, i)
 
    # Extract the elements one by one
    for i in reversed(range(n)):
        arr[0], arr[i] = arr[i], arr[0]
        yield
        yield from __heapify(arr, i, 0)


def quick_sort(arr):
    """Quick sort generator that yields the next indices to be swapped"""
    # Internal function
    def __partition(arr, low, high):
        pivot = arr[high]
        i = low

        for j in range(low, high):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                yield
                i += 1

        arr[i], arr[high] = arr[high], arr[i]
        yield
        return i

    # Internal function
    def __quick_sort(arr, low, high):
        # Sort until the indices cross
        if low < high:
            index = yield from __partition(arr, low, high)
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
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    yield
                    swapped = True
            
            end -= 1  # Decrement the end index
        else: 
            # Going down
            for i in range(end - 1, start - 1, -1): 
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    yield
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
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                yield
                swapped = True
        
        # Even indices
        for i in range(0, size - 1, 2): 
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                yield
                swapped = True


def shell_sort(arr):
    """Shell sort generator that yields the next indices to be swapped"""
    gap = len(arr) // 2

    while gap > 0:
        i = 0
        j = gap

        while j < len(arr):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                yield

            i += 1
            j += 1

            k = i
            while k - gap > -1:
                if arr[k - gap] > arr[k]:
                    arr[k], arr[k - gap] = arr[k - gap], arr[k]
                    yield
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
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            yield
            index -= 1


def pancake_sort(arr):
    """Pancake sort generator that yields the next indices to be swapped"""
    # Internal function
    def __flip(arr, i):
        start = 0

        while start < i:
            arr[i], arr[start] = arr[start], arr[i]
            yield
            start += 1
            i -= 1

    # Start from the complete array and one by one reduce current size by one
    for curr_size in reversed(range(1, len(arr))):
        # Find index of the maximum element in the list
        max_index = arr.index(max(arr[:curr_size]))

        # Move the maximum element to end of the array if it's not already at the end
        if max_index != curr_size - 1:
            # To move at the end, first move the maximum number to the beginning
            yield from __flip(arr, max_index)

            # Now move the maximum number to the end by reversing the current array
            yield from __flip(arr, curr_size)


def stooge_sort(arr):
    """Stooge sort generator that yields the next indices to be swapped"""
    # Internal function
    def __stooge_sort(arr, l, h):
        if l < h:
            # If the first element is smaller than the last, swap them
            if arr[l] > arr[h]:
                arr[l], arr[h] = arr[h], arr[l]
                yield

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
