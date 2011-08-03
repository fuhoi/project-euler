import sys

def printArgs():
	print sys.argv
	
def mod(numerator, denominator):
	return numerator % denominator

def add(x, y):
	return x + y
	
def f(numerators, denominators):
	return [numerator for numerator in numerators for denominator in denominators if mod(numerator, denominator) == 0]
	
def fx(nums):
	total = 0
	for num in nums:
		total += num
	return total
	
if __name__ == "__main__":
	m = 10
	n = 1
	numerators = range(n, m+1)
	denominators = [3, 5]
	nums = f(numerators, denominators)
	print "nums = " + str(nums)
	nums = f(range(1,11), [3,5])
	print "nums = " + str(nums)
	sum = fx(nums)
	print "sum = %s" % sum