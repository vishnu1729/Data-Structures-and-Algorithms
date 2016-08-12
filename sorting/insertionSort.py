""" function to perform insertion sort
the current value of the list to be inserted is stored in a temporary variable currentValue
then it is sequentially compared with the sorted list
the elements are shifted right leading to the creation of a hole which is the place where the current value is to inserted
when a smaller element is found, the shifting right is stopped and inserted in the current position of the hole"""
"""Author: Vishnu Muralidharan"""
def insertionSort(S):
    for index in range(0,len(S)):
        currentValue = S[index]     # current value to be inserted
        holePosition = index        # index of current value
        # till a smaller element is found, keep shifting the elements right 
        while holePosition > 0 and S[holePosition-1] > currentValue:
            S[holePosition] = S[holePosition-1]
            holePosition = holePosition - 1
        S[holePosition] = currentValue  # insert the current element at the current position of the hole


alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)
