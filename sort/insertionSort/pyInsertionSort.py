#!/usr/bin/python3

#Function to do insertion sort
def insertionSort(arr):
    #Traverse the arr
    for i in range(1, len(arr)):
        #initialize key and variable
        key = arr[i]
        j = i - 1
        #loop through array with the conditions
        while j  >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        #insert the key
        arr[j+1] = key

#Test

A = [5, 1, 18, 45, 23, 12]

print("Sorted Array is:")
insertionSort(A)
for i in A:
    print(i)
