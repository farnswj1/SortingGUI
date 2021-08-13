# Imported libraries
import random


def bitonic_sort(arr):
    """Bitonic sort generator"""
    # Internal function
    def __bitonic_merge(arr, low, cnt, up):
        if cnt > 1:
            k = cnt // 2
            for i in range(low, low + k):
                if (up and arr[i] > arr[i + k]) or (not up and arr[i] < arr[i + k]):
                    arr[i], arr[i + k] = arr[i + k], arr[i]
                    yield
            yield from __bitonic_merge(arr, low, k, up)
            yield from __bitonic_merge(arr, low + k, k, up)

    # Internal function
    def __bitonic_sort(arr, low, cnt, up):
        if cnt > 1:
            k = cnt // 2
            yield from __bitonic_sort(arr, low, k, True)
            yield from __bitonic_sort(arr, low + k, k, False)
            yield from __bitonic_merge(arr, low, cnt, up)

    yield from __bitonic_sort(arr, 0, len(arr), True)


def bogo_sort(arr):
    """Bogo sort generator"""
    # Internal function
    def __is_sorted(arr):
        for i in range(1, len(arr)):
            if arr[i - 1] > arr[i]:
                return False
        return True

    # Shuffle until the list is sorted
    while not __is_sorted(arr):
        random.shuffle(arr)
        yield


def bubble_sort(arr):
    """Bubble sort generator"""
    # Start sorting using bubble sort technique
    for i in range(len(arr) - 1):

        # After this iteration max element will come at last
        for j in range(len(arr) - i - 1):

            # Starting element is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                yield


def cocktail_sort(arr):
    """Cocktail sort generator"""
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


def comb_sort(arr):
    """Comb sort generator"""
    # Internal function
    def __get_next_gap(gap):
        # Shrink gap by shrink factor
        gap = (gap * 10) / 13
        return int(gap) if gap >= 1 else 1

    # Initialize gap
    gap = len(arr)

    # Initialize swapped as true to make sure that
    # loop runs
    swapped = True

    # Keep running while gap is more than 1 and last
    # iteration caused a swap
    while gap != 1 or swapped == 1:
        # Find next gap
        gap = __get_next_gap(gap)

        # Initialize swapped as false so that we can check if swap happened or not
        swapped = False

        # Compare all elements with current gap
        for i in range(len(arr) - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                swapped = True
                yield


def gnome_sort(arr):
    """Gnome sort generator"""
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


def heap_sort(arr):
    """Heap sort generator"""
    # Internal function
    def __heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

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

    # Build a maxheap
    for i in reversed(range(len(arr) // 2)):
        yield from __heapify(arr, len(arr), i)

    # Extract the elements one by one
    for i in reversed(range(len(arr))):
        arr[0], arr[i] = arr[i], arr[0]
        yield
        yield from __heapify(arr, i, 0)


def insertion_sort(arr):
    """Insertion sort generator"""
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
    """Merge sort generator"""
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


def odd_even_sort(arr):
    """Odd-even sort generator"""
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


def pancake_sort(arr):
    """Pancake sort generator"""
    # Internal function
    def __flip(arr, i):
        start = 0

        while start < i:
            arr[i], arr[start] = arr[start], arr[i]
            yield
            start += 1
            i -= 1

    # Start from the complete array and one by one reduce current size by one
    for curr_size in reversed(range(1, len(arr) + 1)):
        # Find index of the maximum element in the list
        max_index = arr.index(max(arr[:curr_size]))

        # Move the maximum element to end of the array if it's not already at the end
        if max_index != curr_size - 1:
            # To move at the end, first move the maximum number to the beginning
            yield from __flip(arr, max_index)

            # Now move the maximum number to the end by reversing the current array
            yield from __flip(arr, curr_size - 1)


def quick_sort(arr):
    """Quick sort generator"""
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


def radix_sort(arr):
    """Radix sort generator"""
    # Internal function
    def __counting_sort(arr, exp1):
        # The output array elements that will have sorted arr
        output = [0] * len(arr)

        # initialize count array as 0
        count = [0] * 10

        # Store count of occurrences in count[]
        for i in range(len(arr)):
            index = (arr[i] / exp1)
            count[int(index % 10)] += 1

        # Change count[i] so that count[i] now contains actual
        # position of this digit in output array
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Build the output array
        i = len(arr) - 1
        while i >= 0:
            index = (arr[i] / exp1)
            output[count[int(index % 10)] - 1] = arr[i]
            count[int(index % 10)] -= 1
            i -= 1

        # Copying the output array to arr[],
        # so that arr now contains sorted numbers
        i = 0
        for i in range(0, len(arr)):
            arr[i] = output[i]
            yield

    # Find the maximum number to know number of digits
    max1 = max(arr)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 / exp > 0:
        yield from __counting_sort(arr, exp)
        exp *= 10


def selection_sort(arr):
    """Selection sort generator"""
    for i in range(len(arr)):
        min_idx = i

        # Find the minimum element in the remaining unsorted list
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        yield


def shell_sort(arr):
    """Shell sort generator"""
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


def stooge_sort(arr):
    """Stooge sort generator"""
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
