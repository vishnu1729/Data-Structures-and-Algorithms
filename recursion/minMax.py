# task is to find the max and min of an array of numbers using recursion
# follows a recursive implementation of the iterative mechanism
# author:Vishnu Muralidharan

def maxnum(arr,start,maxArr,minArr):
        # base case: if the array is not of valid length
	if len(arr[start:]) < 1:
		return maxArr, minArr
	else:
                # update the max and min by comparing each element
		if arr[start] >= maxArr:
			maxArr = arr[start]
		if arr[start] <= minArr:
			minArr = arr[start]
		# recursive call 
		return maxnum(arr,start+1,maxArr,minArr)
