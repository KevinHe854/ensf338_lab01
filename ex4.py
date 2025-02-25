import sys
import time
import matplotlib.pyplot as plt
import numpy as np

# Set recursion limit to avoid issues with quicksort
sys.setrecursionlimit(20000)

# Quicksort implementation with counter for number of comparisons
def quicksort(arr, low=0, high=None, comparisons=None):
    if comparisons is None:
        comparisons = [0]  # Use list to allow modification within nested functions
    
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Partition the array
        pivot_index = partition(arr, low, high, comparisons)
        
        # Sort elements before and after the pivot
        quicksort(arr, low, pivot_index - 1, comparisons)
        quicksort(arr, pivot_index + 1, high, comparisons)
    
    return arr, comparisons[0]

def partition(arr, low, high, comparisons):
    # Select the rightmost element as pivot
    pivot = arr[high]
    
    # Index of smaller element
    i = low - 1
    
    for j in range(low, high):
        # Count comparison
        comparisons[0] += 1
        
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            # Increment index of smaller element
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Place pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Generate worst-case input for quicksort (already sorted array with last element as pivot)
def generate_worst_case(size):
    return list(range(size))

# Function to visualize the manual working of quicksort on a worst-case input
def visualize_manual_quicksort():
    # Create a worst-case input of 16 elements
    arr = generate_worst_case(16)
    print("Original array (worst case for quicksort):", arr)
    
    """
    Manual demonstration of quicksort on a sorted array of 16 elements:
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    
    Step 1: Initial call to quicksort(arr, 0, 15)
        Pivot = 15 (last element)
        After partition: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        Pivot index = 15 (no elements moved, as all are already smaller than pivot)
        Recursive calls: quicksort(arr, 0, 14) and quicksort(arr, 16, 15) (second call doesn't execute)
    
    Step 2: Call quicksort(arr, 0, 14)
        Pivot = 14
        After partition: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        Pivot index = 14
        Recursive calls: quicksort(arr, 0, 13) and quicksort(arr, 15, 14) (second call doesn't execute)
    
    Step 3: Call quicksort(arr, 0, 13)
        Pivot = 13
        After partition: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        Pivot index = 13
        Recursive calls: quicksort(arr, 0, 12) and quicksort(arr, 14, 13) (second call doesn't execute)
    
    And so on... Each recursive call reduces the problem size by only 1 element,
    resulting in a total of n-1 partitioning operations, each requiring O(n) comparisons.
    
    This process continues until we reach the base case, resulting in O(n²) complexity.
    """

# Test function for measuring quicksort performance on worst-case inputs
def test_quicksort_worst_case(sizes):
    comparisons_list = []
    times_list = []
    
    for size in sizes:
        print(f"Testing with size: {size}")
        
        # Generate worst-case input
        arr = generate_worst_case(size)
        
        # Measure time and count comparisons
        start_time = time.time()
        _, comparisons = quicksort(arr.copy())
        elapsed_time = time.time() - start_time
        
        comparisons_list.append(comparisons)
        times_list.append(elapsed_time)
    
    return comparisons_list, times_list

# Plot results
def plot_results(sizes, comparisons, times):
    plt.figure(figsize=(12, 10))
    
    # Plot number of comparisons
    plt.subplot(2, 1, 1)
    plt.title('Number of Comparisons in Quicksort (Worst Case)')
    plt.plot(sizes, comparisons, 'bo-', label='Measured Comparisons')
    
    # Fit quadratic function (O(n²))
    coeff = np.polyfit(sizes, comparisons, 2)
    poly = np.poly1d(coeff)
    x = np.linspace(min(sizes), max(sizes), 100)
    plt.plot(x, poly(x), 'r-', label=f'O(n²) fit: {coeff[0]:.2e}n² + {coeff[1]:.2e}n + {coeff[2]:.2e}')
    
    plt.xlabel('Input Size (n)')
    plt.ylabel('Number of Comparisons')
    plt.legend()
    plt.grid(True)
    
    # Plot execution time
    plt.subplot(2, 1, 2)
    plt.title('Execution Time of Quicksort (Worst Case)')
    plt.plot(sizes, times, 'go-', label='Measured Time')
    
    # Fit quadratic function (O(n²))
    coeff = np.polyfit(sizes, times, 2)
    poly = np.poly1d(coeff)
    plt.plot(x, poly(x), 'r-', label=f'O(n²) fit: {coeff[0]:.2e}n² + {coeff[1]:.2e}n + {coeff[2]:.2e}')
    
    plt.xlabel('Input Size (n)')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.savefig('quicksort_worst_case.png')
    plt.show()

# Run the tests
if __name__ == "__main__":
    # Demonstrate manual working of quicksort on worst-case input
    visualize_manual_quicksort()
    
    # Test with various input sizes
    sizes = [100, 200, 300, 400, 500, 750, 1000, 1250, 1500, 1750, 2000]
    comparisons, times = test_quicksort_worst_case(sizes)
    
    # Plot results
    plot_results(sizes, comparisons, times)
    
    """
    Derivation of Worst-Case Complexity for Quicksort:
    
    In the worst case scenario for quicksort:
    1. The pivot chosen at each step results in the most unbalanced partition possible
    2. With last-element pivot selection, this occurs when the array is already sorted
    
    Let's analyze this mathematically:
    
    - Let T(n) be the time complexity for sorting an array of size n
    - In the worst case, each partition operation divides the array into subarrays of size 0 and n-1
    - Each partition operation itself takes O(n) time (to compare each element with the pivot)
    
    This gives us the recurrence relation:
    T(n) = T(n-1) + T(0) + O(n)
    
    Since T(0) = 0, this simplifies to:
    T(n) = T(n-1) + O(n)
    
    Expanding this recursion:
    T(n) = T(n-1) + O(n)
          = T(n-2) + O(n-1) + O(n)
          = T(n-3) + O(n-2) + O(n-1) + O(n)
          ...
          = T(1) + O(2) + O(3) + ... + O(n-1) + O(n)
          = O(1) + O(2) + O(3) + ... + O(n-1) + O(n)
          = O(1 + 2 + 3 + ... + n-1 + n)
          = O(n(n+1)/2)
          = O(n²)
    
    Therefore, the worst-case time complexity of quicksort is O(n²).
    
    Discussion of Results:
    
    The plots confirm our theoretical analysis. When running quicksort on already sorted arrays 
    (with last-element pivot selection), both the number of comparisons and execution time follow 
    a quadratic growth pattern, closely matching the O(n²) curve.
    
    The quadratic fit for both the comparison count and execution time has a dominant n² term,
    which aligns with our derivation of O(n²) worst-case complexity. The minor variations from 
    a perfect quadratic curve can be attributed to system-specific factors and measurement noise.
    
    This worst-case scenario arises because each partition operation only removes one element 
    (the pivot) from consideration, leading to n partitioning operations, each requiring O(n) 
    comparisons. The total is therefore O(n²).
    
    This analysis highlights the importance of good pivot selection strategies in quicksort
    implementations, such as median-of-three or randomized pivot selection, which make this
    worst-case scenario much less likely to occur in practice.
    """