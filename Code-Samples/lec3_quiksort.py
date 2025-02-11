# start = p; end = r;  arr = A
def quickSort(arr, start, end):
    if start < end:
	    # Pick the last element as pivot
        pivot = end
        i = start - 1
        for j in range(start, end):
            if arr[j] <= arr[pivot]:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[pivot] = arr[pivot], arr[i + 1]
        p = i + 1
        quickSort(arr, start, p - 1)
        quickSort(arr, p + 1, end)

arr = [5, 4, 3, 2, 1]
quickSort(arr, 0, len(arr) - 1)
print("Sorted Array in Ascending Order (Method Quicksort): ")
for i in range(len(arr)):
    print(arr[i], end=" ")