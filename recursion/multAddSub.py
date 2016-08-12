# objective is to find the product of two numbers using addition and subtraction
# addition is needed to add n to itself m times
# subtraction is needed to decrement m each time n is added to itself
# author: Vishnu Muralidharan

def mult(m,n,product=0):
	if m > 0:
                # add n to the running sum 
		product += n
		# decrement m and do a recursive call
		return mult(m-1,n,product)
	else:
                # base case when m <= 0
		return product
