"""
Project Euler problem 1 solution
"""

__version__ = "$Revision: 1.0 $"
# $Source$

__author__ = "Adam Lincoln (adam.k.lincoln@gmail.com)"
__date__ = "$Date: 2011/08/03 $"

import sys
import getopt
import functools

def benchmark(func):
    """Print function execution time."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        import time
        t = time.clock()
        res = func(*args, **kwargs)
        #print func.__name__, time.clock()-t
        return res
    return wrapper
    #f = __debug__ and (lambda s: wrapper) or (lambda s: pass_)
    #return  __debug__ and wrapper or pass_

def log(func):
    """Print function details."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        #print func.__name__, args, kwargs
        return res
    return wrapper
    
def counter(func):
    """Print execution count of function."""
    counter.count = 0
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        counter.count = counter.count + 1
        res = func(*args, **kwargs)
        #print func.__name__, "has been used : ", counter.count, "X"
        return res
    return wrapper
    
@counter
@benchmark
@log   
def get_numerators(limit=1000):
    """Return list of numbers from 1 to limit-1."""
    return range(1, limit)

@counter
@benchmark
@log
def get_multiples(numerators, denominators):
    """Return list of numerators divisible by list of denominators."""
    # Find multiples of denominators
    m = [n for n in numerators for d in denominators if is_divisor(n, d)]
    m = list(set(m))  # Remove duplicates
    return m

@counter
@benchmark
@log
def is_divisor(numerator, denominator):
    """Return true if remainder of division is zero."""
    return numerator % denominator == 0

@counter
@benchmark
@log    
def get_total(multiples):
    """ Return total of list."""
    return sum(multiples)

@counter
@benchmark
@log 
def get_answer(limit, denominators):
    """Return solution answer."""
    n = get_numerators(limit)
    m = get_multiples(n, denominators)
    t = get_total(m)
    return t
    
def main():
    # Default values
    n = 1000
    d = [3, 5]
    # Parse parameters
    opts, extraparams = getopt.getopt(sys.argv[1:], "hDn:d:", 
                                      ["help", "debug", "limit=", "limit:", 
                                      "denominators=", "denominators:"])
    # Process parameters
    for o,p in opts:
        if o in ["-h", "--help"]:
            pass # usage()
        if o in ["-D", "--debug"]:
            pass # setDebug()
        if o in ["-n", "--limit"]:
            n = int(p.strip("=:"))
        if o in ["-d", "--denominators"]:
            d = [int(i.strip("=:")) for i in p.split(",")]
    
    a = get_answer(n, d)
    print "Answer: %s" % a

if __name__ == "__main__":
    main()