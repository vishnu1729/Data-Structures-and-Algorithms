# task is to find the integer part of a log2 of a number
# hint: the integer part is the count of how many times a number can be divided by 2
# before a number less than 1 is obtained
# author : Vishnu Muralidharan

def intLog2(n,count):
        #stopping condition for recursion
	if n/2 < 1:
		return count
	else:
        # increment count
		count += 1
		return intLog2(n/2,count) # recur and divide number by 2 once again
