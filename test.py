def findMaximum(arr, low, high):
    if low == high:
        return arr[low]
    if high == low + 1 and arr[low] >= arr[high]:
        return arr[low]
    if high == low + 1 and arr[low] < arr[high]:
        return arr[high]
    mid = (low + high) // 2  # low + (high - low)/2;*/
    if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
        return arr[mid]
    if arr[mid + 1] < arr[mid] < arr[mid - 1]:
        return findMaximum(arr, low, mid - 1)
    else:
        return findMaximum(arr, mid + 1, high)
