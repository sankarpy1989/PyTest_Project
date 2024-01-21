# Python script for implementing Insertion Sort
def insertion_sort(arr):
    # Loop from 1 to arr size
    for i in range(1, len(arr)):
        k = arr[i]
        j = i-1
        while j >= 0 and k < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = k


# Main program to test the above code
arr = [98, 22, 15, 32, 2, 74, 63, 70]
insertion_sort(arr)
print ("Sorted array:")
for i in range(len(arr)):
    print ("% d" % arr[i])