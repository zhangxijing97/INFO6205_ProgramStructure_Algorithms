def find_first_one(arr, left, right):
  if left > right:
    return -1

  mid = left + (right - left) // 2

  if arr[mid] == 1 and (mid == 0 or arr[mid - 1] == 0):
    return mid

  if arr[mid] == 0:
    print("Search in {}".format(arr[mid+1:right+1]))
    return find_first_one(arr, mid + 1, right)  # Search only in the right half
  else:
    print("Search in {}".format(arr[left:mid]))
    return find_first_one(arr, left, mid - 1)  # Search only in the left half 

# Example usage
arr = [0, 0, 0, 1, 1, 1, 1]
arr = [0, 0, 0, 0]
index = find_first_one(arr, 0, len(arr) - 1)
print(f"Index of the first one: {index}") 