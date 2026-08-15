# Linear Search

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

#Binary Search

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1

arr = list(map(int, input("Enter any sorted numbers: ").split()))
key = int(input("Enter element to search: "))

print("\nLinear Search")
index = linear_search(arr, key)

if index != -1:
    print("Element found at index",index)
else:
    print("Element not found")

print("\nBinary Search")
index = binary_search(arr, key)

if index != -1:
    print("Element found at index", index)
else:
    print("Element not found")

