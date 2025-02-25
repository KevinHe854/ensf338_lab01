import sys
import time
import random
import matplotlib.pyplot as plt
import numpy as np

# Set recursion limit to avoid issues with quicksort
sys.setrecursionlimit(20000)

# Linear search implementation
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  # Target not found

# Binary search implementation
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Target not found

# Quicksort implementation
def quicksort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Partition the array
        pivot_index = partition(arr, low, high)
        
        # Sort elements before and after the pivot
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)
    
    return arr

def partition(arr, low, high):
    # Select the rightmost element as pivot
    pivot = arr[high]
    
    # Index of smaller element
    i = low - 1
    
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Place pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Algorithm 1: Just linear search
def algorithm1(arr, target):
    return linear_search(arr, target)

# Algorithm 2: Sort first, then binary search
def algorithm2(arr, target):
    # Sort the array (in worst-case scenario, this is O(n^2) for large n)
    sorted_arr = quicksort(arr.copy())
    return binary_search(sorted_arr, target)

# Generate worst-case input for quicksort
def generate_worst_case_quicksort(size):
    # Already sorted array (worst case for quicksort with last element as pivot)
    return list(range(size))
    # Alternatively, descending:
    # return list(range(size, 0, -1))

# --------------------------------------------------------------------------------
# We will reuse the same function for "average" and "worst" in this example, 
# but always generate a worst-case input for quicksort.

def test_worst_case_quicksort(sizes, num_tasks=100):
    linear_times = []
    sort_binary_times = []
    
    for size in sizes:
        print(f"Testing worst-case quicksort input with size: {size}")
        
        linear_time_total = 0
        sort_binary_time_total = 0
        
        for _ in range(num_tasks):
            # Generate worst-case input for quicksort
            arr = generate_worst_case_quicksort(size)

            # Pick a target from within this sorted array
            target = random.choice(arr)

            # Measure time for linear search
            start_time = time.time()
            algorithm1(arr, target)
            linear_time_total += time.time() - start_time

            # Measure time for sort + binary search
            start_time = time.time()
            algorithm2(arr, target)
            sort_binary_time_total += time.time() - start_time
        
        # Average times over all tasks
        linear_times.append(linear_time_total / num_tasks)
        sort_binary_times.append(sort_binary_time_total / num_tasks)
    
    return linear_times, sort_binary_times

def plot_results(sizes, linear_times, sort_binary_times):
    plt.figure(figsize=(10, 6))
    plt.title('Search Performance Comparison (Worst Case for Quicksort)')
    plt.plot(sizes, linear_times, 'b-', label='Linear Search')
    plt.plot(sizes, sort_binary_times, 'r-', label='Sort + Binary Search')
    plt.xlabel('Input Size')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)
    
    # Attempt to find a crossover point
    crossover = None
    for i in range(len(sizes) - 1):
        if linear_times[i] <= sort_binary_times[i] and linear_times[i+1] > sort_binary_times[i+1]:
            crossover = sizes[i]
            plt.axvline(x=crossover, color='g', linestyle='--', label=f'Crossover at {crossover}')
            break
    
    plt.savefig('search_performance_worst_case_quicksort.png')
    plt.show()
    
    return crossover

if __name__ == "__main__":
    # Input sizes to test
    sizes = [10, 20, 50, 100, 200, 500, 1000]
    
    # Test worst-case performance for quicksort
    linear_times, sort_binary_times = test_worst_case_quicksort(sizes, num_tasks=50)
    crossover = plot_results(sizes, linear_times, sort_binary_times)
    
    if crossover:
        print(f"Sort+Binary Search becomes faster than Linear Search at around {crossover} elements (worst-case).")
    else:
        # Check if one algorithm is always faster
        if linear_times[-1] < sort_binary_times[-1]:
            print("Linear Search is always faster within these tested sizes.")
        else:
            print("Sort+Binary Search eventually becomes faster for large inputs, even in the worst-case.")
            
 

    """
    Worst Case Analysis (for Quicksort):
    
    When using inputs that trigger quicksort's worst-case behavior:
    
    1. Linear search still has O(n) complexity.
    
    2. The "sort first, then binary search" approach now has O(n²) + O(log n) complexity
       due to quicksort's worst-case performance, which is dominated by the O(n²) sorting step.
    
    3. This makes the sort-first approach significantly worse than direct linear search
       for practically all array sizes we tested.
    
    4. The crossover point, if it exists, would be at a much larger array size than in the
       average case scenario, potentially making linear search the better choice for most
       practical applications when dealing with this specific type of input.
    
    These results highlight how the choice of search algorithm depends not just on array size,
    but also on the nature of the input data and the specific implementation of the sorting algorithm.
    For inputs that trigger quicksort's worst-case behavior, linear search is clearly superior
    across the tested range of array sizes.
    """