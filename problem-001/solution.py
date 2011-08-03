"""Project Euler problem 1 solution"""

__author__ = "Adam Lincoln (adam.k.lincoln@gmail.com)"
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 2011/08/03 $"

def __remainder(numerator, denominator):
    """Returns the remainder of the numerator divided by the denominator"""
    return numerator % denominator

def __divisors(numerators, denominators):
    """Returns a list of numerators that are divisible by a list of denominators"""
    return [n for n in numerators for m in denominators if __remainder(n, m) == 0]

if __name__ == "__main__":
    # print file information
    print "%s\n---" %__doc__
    
    # min and max variables
    min = 1
    max = 10 # max is less than condition
    
    # create numerators, denominators, divisors and total
    numerators = range(min, max)
    denominators = [3, 5]
    divisors = __divisors(numerators, denominators)
    total = sum(divisors)
    
    # print out debug info
    if __debug__:
        print "The numerators used are %s" % numerators
        print "The denominators used are %s" % denominators
        print "The divisors used are %s" % divisors
    
    # print out final result
    print "The sum of numbers between %s and %s that is divisible by %s is %s" % (min, max, "%s and %s" % (", ".join(str(d) for d in denominators[:-1]), denominators[-1]), total)