#!/usr/bin/python3

#function that partion the unsorting list
def partition(arr, start, end):
    pIndex = start #index of smaller element
    pivot = arr[end] #last element as the pivot

    for j in range(start, end):
        if arr[j] <= pivot:
            arr[pIndex], arr[j] = arr[j], arr[pIndex] #swap the index
            pIndex += 1
    
    arr[pIndex], arr[end] = arr[end], arr[pIndex]
    return pIndex
    
#Quick Sort Function
def quickSort(arr, start, end):
    if start < end:
        pi = partition(arr, start, end)

        quickSort(arr, start, pi-1)
        quickSort(arr, pi+1, end)

#Driver code to test
arr = [10, 7, 23, 34, 42, 18]
n = len(arr)
quickSort(arr, 0, n-1)

print("Sorted array is:")
print(arr)
    
            
