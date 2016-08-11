""" function to perform selection sort
a small modification over bubble sort
in each pass the minimum element is obtained
and inserted in the list beginning from the leftmost position"""
"""Author: Vishnu Muralidharan"""

def selectionSort(S):
    for insertSlot in range(0,len(S)-1,1):  # loop to keep track of slot to be inserted
        posMin = insertSlot
        for index in range(insertSlot+1,len(S)): #loop over the rest of the list to find the minimum element
            if S[index] < S[posMin]:
                posMin = index              # if minimum element is found, posMin is the index of the minimum element
        # swap the minimum element and the element at the position to be inserted
        temp = S[insertSlot]
        S[insertSlot] = S[posMin]
        S[posMin] = temp



alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)
