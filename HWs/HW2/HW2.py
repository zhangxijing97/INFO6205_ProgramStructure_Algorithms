def find_rotation_count(arr):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        # If the array is already sorted
        if arr[low] <= arr[high]:
            return low
        
        mid = (low + high) // 2
        next_idx = (mid + 1) % len(arr)
        prev_idx = (mid - 1 + len(arr)) % len(arr)

        # Check if mid is the pivot
        if arr[mid] <= arr[next_idx] and arr[mid] <= arr[prev_idx]:
            return mid
        
        # Search in the unsorted half
        if arr[mid] >= arr[low]:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Should not reach here

# Example Test Cases
arr1 = [15, 18, 2, 3, 6, 12]
arr2 = [7, 9, 11, 12, 5]

print("Rotation count for arr1:", find_rotation_count(arr1))  # Expected output: 2
print("Rotation count for arr2:", find_rotation_count(arr2))  # Expected output: 4