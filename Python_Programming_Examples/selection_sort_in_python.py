# Python script for implementing Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        # Find the min
        min = i
        for j in range(i + 1, len(arr)):
            if arr[min] > arr[j]:
                min = j

        tmp = arr[i]
        arr[i] = arr[min]
        arr[min] = tmp
    return arr


# Main program to test the above code
arr = [98, 22, 15, 32, 2, 74, 63, 70]

selection_sort(arr)

print("Sorted array: ")
for i in range(len(arr)):
    print("%d" % arr[i])


