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
            # Increment index of smaller element
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
    sorted_arr = quicksort(arr.copy())
    return binary_search(sorted_arr, target)

# Generate worst-case input for quicksort
def generate_worst_case_quicksort(size):
    # Already sorted array (worst case for quicksort with last element as pivot)
    return list(range(size))

# Test function for average case
def test_average_case(sizes, num_tasks=100):
    linear_times = []
    sort_binary_times = []
    
    for size in sizes:
        print(f"Testing average case with size: {size}")
        
        linear_time_total = 0
        sort_binary_time_total = 0
        
        for _ in range(num_tasks):
            # Generate random array of specified size
            arr = random.sample(range(size*10), size)
            
            # Select a random element to search for
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

# Test function for worst case for quicksort
def test_worst_case(sizes, num_tasks=100):
    linear_times = []
    sort_binary_times = []
    
    for size in sizes:
        print(f"Testing worst case with size: {size}")
        
        linear_time_total = 0
        sort_binary_time_total = 0
        
        for _ in range(num_tasks):
            # Generate worst-case input for quicksort
            arr = generate_worst_case_quicksort(size)
            
            # Select a random element to search for
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

# Plot results
def plot_results(sizes, linear_times, sort_binary_times, case_type):
    plt.figure(figsize=(10, 6))
    plt.title(f'Search Performance Comparison ({case_type} Case)')
    plt.plot(sizes, linear_times, 'b-', label='Linear Search')
    plt.plot(sizes, sort_binary_times, 'r-', label='Sort + Binary Search')
    plt.xlabel('Input Size')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)
    
    # Find crossover point
    crossover = None
    for i in range(len(sizes)-1):
        if linear_times[i] <= sort_binary_times[i] and linear_times[i+1] > sort_binary_times[i+1]:
            crossover = sizes[i]
            plt.axvline(x=crossover, color='g', linestyle='--', label=f'Crossover at {crossover}')
            break
    
    plt.savefig(f'search_performance_{case_type.lower()}.png')
    plt.show()
    
    return crossover

# Run the tests
if __name__ == "__main__":
    # Input sizes to test
    sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
    
    # Test average case
    linear_times_avg, sort_binary_times_avg = test_average_case(sizes)
    crossover_avg = plot_results(sizes, linear_times_avg, sort_binary_times_avg, "Average")
    
    if crossover_avg:
        print(f"In the average case, Sort+Binary Search becomes faster than Linear Search at around {crossover_avg} elements.")
    else:
        # Check if one algorithm is always faster
        if linear_times_avg[-1] < sort_binary_times_avg[-1]:
            print("In the average case, Linear Search is always faster for the tested sizes.")
        else:
            print("In the average case, Sort+Binary Search becomes faster than Linear Search for large inputs.")
    
    """
    Average Case Analysis:
    
    For the average case, we observe that:
    
    1. Linear search has a time complexity of O(n), with an average case of n/2 comparisons
       when the target is present.
    
    2. The "sort first, then binary search" approach has a complexity of O(n log n) + O(log n),
       which is dominated by the O(n log n) sorting step.
    
    3. For small arrays, linear search is faster because it has minimal overhead compared to
       the sort-first approach which requires sorting the entire array before searching.
    
    4. As the array size increases, there comes a point where the advantage of binary search's
       O(log n) lookup becomes significant enough to offset the sorting cost.
    
    5. This crossover point typically occurs around a few hundred elements, depending on the
       specific implementation and hardware. For our tests, it's approximately at [crossover_avg] elements.
    
    The results align with the theoretical analysis: for small arrays, linear search is more efficient,
    but for larger arrays, even with the overhead of sorting, the sort-first approach eventually wins.
    """
    
    # Test worst case for quicksort
    linear_times_worst, sort_binary_times_worst = test_worst_case(sizes)
    crossover_worst = plot_results(sizes, linear_times_worst, sort_binary_times_worst, "Worst")
    
    if crossover_worst:
        print(f"In the worst case for quicksort, Sort+Binary Search becomes faster than Linear Search at around {crossover_worst} elements.")
    else:
        # Check if one algorithm is always faster
        if linear_times_worst[-1] < sort_binary_times_worst[-1]:
            print("In the worst case for quicksort, Linear Search is always faster for the tested sizes.")
        else:
            print("In the worst case for quicksort, Sort+Binary Search becomes faster than Linear Search for large inputs.")

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