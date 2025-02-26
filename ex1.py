import sys
sys.setrecursionlimit(20000)

def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid+1, high)
        merge(arr, low, mid, high)
        
def merge(arr, low, mid, high):
    size_left = mid - low + 1
    size_right = high - mid
    
    # Add elements into left and right subarrays
    left_subarr = [0] * size_left
    right_subarr = [0] * size_right
    
    for i in range(0, size_left):
        left_subarr[i] = arr[low + i]
        
    for j in range(0, size_right):
        right_subarr[j] = arr[mid + 1 + j]
        
    # Merge subarrays
    index_left = 0
    index_right = 0
    index_arr = low
    
    while index_left < size_left and index_right < size_right:
        if left_subarr[index_left] <= right_subarr[index_right]:
            arr[index_arr] = left_subarr[index_left]
            index_left += 1
        else:
            arr[index_arr] = right_subarr[index_right]
            index_right += 1
        index_arr += 1
        
    # If right_subarr is all done, finish left_subarr
    while index_left < size_left:
        arr[index_arr] = left_subarr[index_left]
        index_left += 1
        index_arr += 1
        
    # If left_subarr is done, finish right_subarr
    while index_right < size_right:
        arr[index_arr] = right_subarr[index_right]
        index_right += 1
        index_arr += 1



arr = [8, 42, 25, 3, 3, 2, 27, 3]

merge_sort(arr, 0, len(arr)-1)

print(arr)
