def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_idx=i
        for j in range(i+1,n):
            if arr[j] < arr[min_idx]:
                min_idx=j
        arr[i],arr[min_idx] = arr[min_idx],arr[i]  

def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x==pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


input_list = list(map(int, input("Enter elements separated by space: ").split()))
print("Input list:", input_list)

arr = input_list[:]

bubble_sort(arr)
print("Bubble Sorted List:", arr)

arr = input_list[:]

selection_sort(arr)
print("Selection Sorted List:", arr)

arr = input_list[:]

insertion_sort(arr)
print("Insertion Sorted List:", arr)

arr = input_list[:]

arr = quick_sort(arr)
print("Quick Sorted List:", arr)