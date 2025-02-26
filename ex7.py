# Question 4: The choice of initial midpoints does seem to affect the
# performance very slightly (the changes are microseconds big). However
# the standard binary search seems to be the fastest, albeit very
# slightly. This is probably because cutting the array doing
# interpolation search initially has a chance of leaving our key in
# the bigger half. This can greatly increase the size of the array we
# then have to search next, especially if we then cut the array in half
# every time afterwards.

import timeit
import json
from matplotlib import pyplot as plt
from math import ceil
import random

def binary_search(arr, key, midpoints):
    low = 0
    high = len(arr) - 1
    
    # Start at the middle
    # mid = (low + high) // 2
    
    # Pick randomly
    # mid = random.randint(low, high)
    
    # Interpolate
    p = (key - arr[low]) / (arr[high] - arr[low])
    mid = low + ceil((high - low) * p)
    
    midpoints.append(mid)
    
    while low <= high:
        if key < arr[mid]:
            high = mid - 1
        elif arr[mid] < key:
            low = mid + 1
        else:
            return mid
        mid = (low + high) // 2
    
    return -1

with open('ex7data.json', 'r', encoding='UTF-8') as file:
    data = json.load(file)
    
with open('ex7tasks.json', 'r', encoding='UTF-8') as file:
    tasks = json.load(file)

midpoints = []
times = []

for i in tasks:
    times.append(timeit.timeit(setup='from __main__ import binary_search, data, i, midpoints',
                                stmt='binary_search(data, i, midpoints)',
                                number=1))

for i in range(len(times)):
    times[i] *= 1000000

# Plotting Time vs Tasks
plt.subplot(1, 2, 1)
plt.scatter(tasks, times)
plt.xlabel("Tasks")
plt.ylabel("Time (microseconds)")

# Plotting Midpoints vs Tasks
plt.subplot(1, 2, 2)
plt.scatter(tasks, midpoints)
plt.xlabel("Tasks")
plt.ylabel("Starting Midpoint")

plt.show()