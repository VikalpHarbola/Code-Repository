def binarySearch(arr,l,r,x):
    #check base case
    if r>=l:
        mid=l+(r-l)//2

        #if element is present in middle itself
        if arr[mid]==x:
            return mid
        #if element is smaller than middle element then it can only be present in left subarray
        elif arr[mid]>x:
            return binarySearch(arr,l,mid-1,x)
        # if element is greater than middle element then it can only be present in right subarray
        else:
            return binarySearch(arr,mid+1,r,x)
    else:
        # element is not present in array
        return -1

if __name__ == '__main__':
    # Driver Code
    arr=[2,3,4,10,40]
    x=10
    # Function call
    result=binarySearch(arr,0,len(arr)-1,x)
    if result!=-1:
        print("Element is present at index % d" % result)
    else:
        print("Element is not present in array")