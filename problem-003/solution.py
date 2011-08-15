"""
Project Euler problem 3 solution
"""

__version__ = "$Revision: 1.0 $"
# $Source$

__author__ = "Adam Lincoln (adam.k.lincoln@gmail.com)"
__date__ = "$Date: 2011/08/015 $"

import sys
import getopt
import functools

def log(func):
    """Print function details."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print func.__name__, args, kwargs
        res = func(*args, **kwargs)
        return res
    return wrapper

@log    
def fib(f):
    """Return sum of penultimate and ultimate numbers in list"""
    s = sum(f[-2:])
    print "returned %s" % s
    return s

@log
def get_answer(limit):
    """Return solution answer."""
    #initialise
    f = [1, 2]
    e = [2]
    # main loop
    #for i in range(1, limit - 1):
    i = fib(f)
    while i < limit:
        f.append(i)
        if i % 2 == 0:
            e.append(i)
        i = fib(f)
    print "list %s" % f
    print "list %s" % e
    s = sum(e)
    return s
    
def main():
    # Default values
    l = 10
    # Parse parameters
    opts, extraparams = getopt.getopt(sys.argv[1:],
                                      "v:l:",
                                      ["verbosity:", "limit="])
    # Process parameters
    for o,p in opts:
        if o in ["-v", "--verbosity"]:
            pass # setDebug()
        if o in ["-l", "--limit"]:
            l = int(p.strip("=:"))
    # find answer
    a = get_answer(l)
    print "Answer: %s" % a

if __name__ == "__main__":
    main()