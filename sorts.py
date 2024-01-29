Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def insertion_sort(arr):
...   for i in range(1, len(arr)):
...     key = arr[i]
...     j = i-1
...     while j >= 0 and key < arr[j]:
...       arr[j + 1] = arr[j]
...       j -= 1
...     arr[j + 1] = key
... 
... def selection_sort(arr):
...   for i in range(len(arr)):
...     min_idx = i
...     for j in range(i+1, len(arr)):
...       if arr[min_idx] > arr[j]:
...         min_idx = j        
...     arr[i], arr[min_idx] = arr[min_idx], arr[i]
... 
... def bubble_sort(arr):
...   n = len(arr)
...   for i in range(n):
...     for j in range(0, n-i-1):
...       if arr[j] > arr[j+1]:
