"""
Project Euler problem 1 solution
"""

import sys
import getopt
import functools

__author__ = "Adam Lincoln (adam.k.lincoln@gmail.com)"
__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 2011/08/03 $"

def benchmark(func):
    """
    A decorator that print the time of function take
    to execute.
    """
    import time
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print func.__name__, time.clock()-t
        return res
    return wrapper

def log(func):
    """
    A decorator that logs the activty of the script.
    Ok, it really just print it, put it could be loggin!
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print func.__name__, args, kwargs
        return res
    return wrapper

def counter(func):
    """
    A decorator that print the number of time a function has been executed
    """
    counter.count = 0
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        counter.count = counter.count + 1
        res = func(*args, **kwargs)
        print func.__name__, "has been used : ", counter.count, "X"
        return res
    return wrapper

@counter
@benchmark
@log
def remainder(numerator, denominator):
    """
    Returns the remainder of the numerator divided by the denominator
    """
    return numerator % denominator

@counter
@benchmark
@log
def isDivisor(numerator, denominator):
    """
    Returns true if the remainder of the division is zero
    """
    return remainder(numerator, denominator) == 0

@counter
@benchmark
@log
def multiples(numerators, denominators):
    """
    Returns a list of numerators that are divisible by a list of denominators
    """
    
    # find multiples of denominators
    m = [n for n in numerators for d in denominators if isDivisor(n, d)]
    
    # remove duplicates
    m = list(set(m))
    
    return m

@counter
@benchmark
@log
def main:
    """
    Main method
    """
    
    # print file information
    print "%s\n---" %__doc__
    
    # parse parameters
    opts, extraparams = getopt.getopt(sys.argv[1:], "hDn:d:", ["help", "debug", "limit=", "limit:", "denominators=", "denominators:"])
    
    # default min and max variables
    min = 1
    max = 10
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
        print "Numerators are %s" % n
        print "Denominators are %s" % d
        print "Multiples are %s" % m
    
    # print out final result
    print "The sum of numbers between %s and %s that is divisible by %s is %s" % (min, max, "%s and %s" % (", ".join(str(d) for d in d[:-1]), d[-1]), t)

if __name__ == "__main__":
    main()