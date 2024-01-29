Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import timeit
import random

# Function to benchmark
def benchmark_sorting_algorithm(algorithm, array):
    return timeit.timeit(lambda: algorithm(array.copy()), number=1000)

# Insertion Sort
... def insertion_sort(array):
...     for i in range(1, len(array)):
...         key = array[i]
...         j = i - 1
...         while j >= 0 and array[j] > key:
...             array[j + 1] = array[j]
...             j -= 1
...         array[j + 1] = key
... 
... # Selection Sort
... def selection_sort(array):
...     for i in range(len(array)):
...         min_index = i
...         for j in range(i + 1, len(array)):
...             if array[j] < array[min_index]:
...                 min_index = j
...         array[i], array[min_index] = array[min_index], array[i]
... 
... # Bubble Sort
... def bubble_sort(array):
...     n = len(array)
...     for i in range(n):
...         for j in range(0, n - i - 1):
...             if array[j] > array[j + 1]:
...                 array[j], array[j + 1] = array[j + 1], array[j]
... 
... 
... sizes = [5, 10, 20, 50, 100, 200, 500, 1000,2000,5000,10000,100000]
... 
... for size in sizes:
...     array = [random.randint(1, 1000) for _ in range(size)]
...     
...     time_taken = benchmark_sorting_algorithm(insertion_sort, array)
...     print(f"Insertion Sort - Array Size {size}: {time_taken:.6f} seconds")
...     
...     time_taken = benchmark_sorting_algorithm(selection_sort, array)
...     print(f"Selection Sort - Array Size {size}: {time_taken:.6f} seconds")
...     
...     time_taken = benchmark_sorting_algorithm(bubble_sort, array)
