from matplotlib import pyplot as plt

def bubble_sort(arr, len_arr, comp_arr, swap_arr):
    n = len(arr)
    comp = 0
    swap = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swap += 1
            comp += 1
        
    print("Number of comparisons:", comp)
    print("Number of swaps:", swap)
    
    len_arr.append(n)
    comp_arr.append(comp)
    swap_arr.append(swap)
    
    return arr

len_arr = []
comp_arr = []
swap_arr = []

print(bubble_sort([], len_arr, comp_arr, swap_arr))
print(bubble_sort([7,2,4], len_arr, comp_arr, swap_arr))
print(bubble_sort([6,2,9,8,1], len_arr, comp_arr, swap_arr))
print(bubble_sort([29,82,63,16,60,91,41], len_arr, comp_arr, swap_arr))
print(bubble_sort([111,332,862,752,731,915,182,394,723], len_arr, comp_arr, swap_arr))
print(bubble_sort([672,391,681,112,739,448,922,614,829,459,392], len_arr, comp_arr, swap_arr))

plt.plot(len_arr, comp_arr)
plt.title("Comparisons to Length")
plt.xlabel("Array Length")
plt.ylabel("Number of Comparisons")
plt.show()

plt.plot(len_arr, swap_arr)
plt.title("Swaps to Length")
plt.xlabel("Array Length")
plt.ylabel("Number of Swaps")
plt.show()
