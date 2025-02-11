def countingSort(array, place):
    size = len(array)
    output = [0] * size

    # Initialize count array (heuristic)
    count = [0] * 10

    # Store the count of each elements in count array
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    # Store the cummulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]

# Main function to implement radix sort
def radixSort(array):
    # Get maximum element
    max_element = max(array)

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10


arr = [5, 4, 3, 2, 1]
arr = [121, 432, 564, 23, 1, 45, 788]
radixSort(arr)
print("Sorted Array in Ascending Order (radix sort): ")
print(arr)
