""" script for quicksort algorithm.
reference: mycodeschool.com
the vairable pIndex is the partition index or the index of the pivot after the list had been sorted
it is initialized to the start of a given list and eventually moved throguht the lisr till it meets the pivot
since recusrion is used, start and end indices of the sequences to be sorted are passed as arguments to the functions
maitaining the start and end indices is also necessary since we sort the list in place to reduce space complexity"""
"""Author: Vishnu Muralidharan"""

# the quickSort function is the recursive implementation of the quicksort algorithm 
def quickSort(aList,start,end):
    if start < end:     # base case for recursion:stop recursion if the sequence is one element long or empty
        pIndex = partition(aList,start,end) #return the index of the pivot element
        quickSort(aList,start,pIndex-1) #quicksort the sequence less than the pivot
        quickSort(aList,pIndex+1,end)   #quciksort the sequence greater than the pivot

# the partition function splits the list such that elements to the left of the pivot are less than the pivot
# and the elements of the right of the pivot are greater than the pivot
def partition(aList,start,end):
    pivot = aList[end]      # the pivot is chosen as the last element of the sequence
    pIndex = start          # set partition index at start, it will eventually meet the pivot
    for i in range(start,end):
        if aList[i] <= pivot:   # if the current element is less than the pivot swap
            temp = aList[i]
            aList[i] = aList[pIndex]
            aList[pIndex] = temp
            #swap(aList[i],aList[pIndex])
            pIndex += 1         # increment pIndex, this helps in the pIndex meeting the pivot

    # now the list is such that the pivot is at the end of the list and the left and right elements are in correct positions
    # now swap the latest pIndex with the pivot for the correct ordering
    temp = aList[pIndex]
    aList[pIndex] = aList[end]
    aList[end] = temp
    return pIndex



alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist,0,len(alist)-1)
print(alist)
            
