def bubbleSort(arr):
    # Python program for implementation of Bubble Sort
    n=len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            print(f"i: {i}, j: {j}")
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]


if __name__=="__main__":
    arr = [5, 1, 4, 2, 8,3]

    bubbleSort(arr)

    print("Sorted array is:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")