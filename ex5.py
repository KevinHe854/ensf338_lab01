# The answer to question 4 is that on average, binary insertion sort is
# faster when the array length is small, but insertion sort is faster
# when the array length is larger. This is because binary searching
# works best on a mostly sorted array, which is not necessarily the case
# in an average case scenario with random ordering.

import sys
import timeit
from matplotlib import pyplot as plt
sys.setrecursionlimit(20000)

# Implementing insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    print(arr)

# Implementing binary insertion sort
def binary_search(arr, key, start, end):
    if start == end:
        if arr[start] > key:
            return start
        else:
            return start + 1
    
    if start > end:
        return start
    
    mid = (start + end) // 2
    if arr[mid] < key:
        return binary_search(arr, key, mid+1, end)
    elif arr[mid] > key:
        return binary_search(arr, key, start, mid-1)
    else:
        return mid

def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = binary_search(arr, key, 0, i-1)
        arr = arr[:j] + [key] + arr[j:i] + arr[i+1:]
    print(arr)

len_arr = [4, 5, 7, 8, 10, 12, 15]
insert_times = []
bin_times = []

isetup = 'from __main__ import insertion_sort'
bsetup = 'from __main__ import binary_insertion_sort'

i4 = 'insertion_sort([62,13,81,24])'
i5 = 'insertion_sort([92,12,47,53,28])'
i7 = 'insertion_sort([73,91,13,42,27,34,56])'
i8 = 'insertion_sort([63,29,51,81,69,47,19,33])'
i10 = 'insertion_sort([532,823,645,136,639,239,836,534,341,729])'
i12 = 'insertion_sort([562,913,612,123,832,724,327,539,823,283,901,734])'
i15 = 'insertion_sort([613,813,173,931,471,209,816,953,351,293,492,592,284,682,520])'

b4 = 'binary_insertion_sort([62,13,81,24])'
b5 = 'binary_insertion_sort([92,12,47,53,28])'
b7 = 'binary_insertion_sort([73,91,13,42,27,34,56])'
b8 = 'binary_insertion_sort([63,29,51,81,69,47,19,33])'
b10 = 'binary_insertion_sort([532,823,645,136,639,239,836,534,341,729])'
b12 = 'binary_insertion_sort([562,913,612,123,832,724,327,539,823,283,901,734])'
b15 = 'binary_insertion_sort([613,813,173,931,471,209,816,953,351,293,492,592,284,682,520])'

insert_times.append(timeit.timeit(setup=isetup, stmt=i4, number=1))
insert_times.append(timeit.timeit(setup=isetup, stmt=i5, number=1))
insert_times.append(timeit.timeit(setup=isetup, stmt=i7, number=1))
insert_times.append(timeit.timeit(setup=isetup, stmt=i8, number=1))
insert_times.append(timeit.timeit(setup=isetup, stmt=i10, number=1))
insert_times.append(timeit.timeit(setup=isetup, stmt=i12, number=1))
insert_times.append(timeit.timeit(setup=isetup, stmt=i15, number=1))

bin_times.append(timeit.timeit(setup=bsetup, stmt=b4, number=1))
bin_times.append(timeit.timeit(setup=bsetup, stmt=b5, number=1))
bin_times.append(timeit.timeit(setup=bsetup, stmt=b7, number=1))
bin_times.append(timeit.timeit(setup=bsetup, stmt=b8, number=1))
bin_times.append(timeit.timeit(setup=bsetup, stmt=b10, number=1))
bin_times.append(timeit.timeit(setup=bsetup, stmt=b12, number=1))
bin_times.append(timeit.timeit(setup=bsetup, stmt=b15, number=1))

for i in range(len(insert_times)):
    insert_times[i] *= 1000
    
for i in range(len(bin_times)):
    bin_times[i] *= 1000
    
plt.plot(len_arr, insert_times, color='r', label='Insertion times')
plt.plot(len_arr, bin_times, color='b', label='Binary insertion times')
plt.legend()

plt.xlabel('Array Length')
plt.ylabel("Time (milliseconds)")
plt.show()