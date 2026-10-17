def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

if __name__ == "__main__":
    sample_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    query = 23
    result = binary_search(sample_list, query)
    print(f"Index of {query} in {sample_list}: {result}")
