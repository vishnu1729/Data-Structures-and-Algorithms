"""function definitions to perform merge sort on the given list.
The merge function takes care of the actual sorting and merges the sublists.
The mergeSort function takes care of the recursion mechanism used to
sort the left and right halves of the given list"""
"""Author: Vishnu Muralidharan"""


# function to sort and merge the sublists S1, S2 into a merged list S
def merge(S1,S2,S):
    i=j=0
    while i < len(S1) and j < len(S2):
        if S1[i] < S2[j]:       # compare the respective elements in both the sublists
            S[i+j] = S1[i]      # assign the lesser element to the current index in the merged list
            i += 1
        else:
            S[i+j] = S2[j]      # assign the lesser element to the current index in the merged list
            j += 1

# functio to recur on the left and right sublists
# the recusrion tree generated stops when each of the sublists is one element long
# the control comes out of the recusrion and calls merge() function to merge the respective elements
def mergeSort(S):
    # stopping condition for recursion
    if len(S) < 2:
        return
    mid = len(S)//2     # get middle index
    S1 = S[:mid]        # get the left half of the list 
    S2 = S[mid+1:]      # get the right half of the list
    mergeSort(S1)       # recur on the left half of the list 
    mergeSort(S2)       # recur on the right half of the list
    merge(S1,S2,S)      # sort and merge the left and right halves
