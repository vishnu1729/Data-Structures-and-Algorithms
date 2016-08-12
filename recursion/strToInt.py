# Objective: to convert a string to its equivalent integer
# The string is processed from left to right
# Each character at the current position is multiplied by 10^(position) to get the place value
# all the obtained place values are added to get the integer
# author:Vishnu Muralidharan

def strToInt(numStr,start):
        # base case if string is empty return 0
	if len(numStr[start:]) == 0:
		return 0
	else:
                # compute the place value of the string's current position
		num = int(numStr[start])*(10**(len(numStr[start:])-1))
		# recursive call to process the remaining digits
		return num + strToInt(numStr,start+1)
