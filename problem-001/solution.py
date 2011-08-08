"""Project Euler problem 1 solution"""

import sys
import getopt

__author__ = "Adam Lincoln (adam.k.lincoln@gmail.com)"
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 2011/08/03 $"

def remainder(numerator, denominator):
    """Returns the remainder of the numerator divided by the denominator"""
    return numerator % denominator

def isDivisor(numerator, denominator):
    """Returns true if the remainder of the division is zero"""
    return remainder(numerator, denominator) == 0
    
def multiples(numerators, denominators):
    """Returns a list of numerators that are divisible by a list of denominators"""
    m = []
    for n in numerators:
        for d in denominators:
            if isDivisor(n, d):
                m.append(n)
    m = list(set(m)) # remove duplicates
    return m

if __name__ == "__main__":
    # print file information
    print "%s\n---" %__doc__
    # parse parameters
    opts, extraparams = getopt.getopt(sys.argv[1:], "hDn:d:", ["help", "debug", "limit=", "limit:", "denominators=", "denominators:"])
    # default min and max variables
    min = 1
    max = 10 # max is less than condition
    d = [3, 5]
    # process parameters
    for o,p in opts:
        if o in ["-h", "--help"]:
            pass # usage()
        if o in ["-D", "--debug"]:
            pass # setDebug()
        if o in ["-n", "--limit"]:
            max = int(p.strip("=:"))
        if o in ["-d", "--denominators"]:
            d = [int(i.strip("=:")) for i in p.split(",")]
    # create numerators, multiples and total
    n = range(min, max)
    m = multiples(n, d)
    t = sum(m)
    # sort for display
    n.sort()
    m.sort()
    # print out debug info
    if __debug__:
        print "The numerators used are %s" % n
        print "The denominators used are %s" % d
        print "The multiples used are %s" % m
    # print out final result
    print "The sum of numbers between %s and %s that is divisible by %s is %s" % (min, max, "%s and %s" % (", ".join(str(d) for d in d[:-1]), d[-1]), t)