"""function to use recusrion to search for an element in a sorted array."""
"""Author: Vishnu Muralidharan"""


def binarySearch(data,target,low,high):
    # stop condition for recursion
    if low > high:
        return None
    mid = (low + high)//2       # get the middle index of array

    if target == data[mid]:     # if the element to be found is at the middle index
        return mid
    elif target < data[mid]:    # if the target is less than the element at middle index
        return binarySearch(data,target,low,mid - 1)    # recur binary search over the left half of the array
    else:
        return binarySearch(data,target,mid+1,high)     # else recur over the right half of the array



arr = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
search = 22
index = binarySearch(arr,search,0,len(arr))
print("data found at %d" % index)
