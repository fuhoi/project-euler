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
import math

def log(func):
    """Print function details."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print func.__name__, args, kwargs
        res = func(*args, **kwargs)
        return res
    return wrapper

# @log
def is_divisor(numerator, denominator):
    """Return true if remainder of division is zero."""
    return numerator % denominator == 0
    
# @log
def is_prime(n):
    """Return true if number is prime"""
    # even is not prime
    # NOTE: Do not even process even numbers fool
    if n % 2 == 0:
        #print "%s is not prime" % n
        return False
    # everything is divisible by 1 so don't test that
    # we just tested 2 so start at 3
    # n is not going to be divisible after floor(n / 2) so end there (don't waste time after that)
    for d in range(3, int(math.floor(n / 2))):
        if is_divisor(n, d):
            #print "%s is not a prime" % n
            return False # Number is divisible, not prime
    else: # No divisors
        #print "%s is a prime" % n
        return True # Prime!
    return False # Shouldn't get here

# @log
def get_prime_numbers(max):
    """Return list of prime numbers."""
    #initialise
    p = []
    i = 0
    # main loop
    #for i in range(int(max+1)):
    while i < int(max+1):
        if is_prime(i):
            p.append(i)
        i += 1
    #print "list %s" % p
    return p
    
# @log
def get_answer(number):
    """Return solution answer."""
    # initialise
    f = [] # Factors
    p = get_prime_numbers(int(math.floor(number / 2))) # Primes
    # main loop
    for i in p:
        if is_divisor(number, i):
            f.append(i)
    #print "list %s" % i
    #print "largest %s" % f[-1:]
    return sum(f[-1:])

@log
def main():
    # Default values
    n = 13195
    # Parse parameters
    opts, extraparams = getopt.getopt(sys.argv[1:],
                                      "v:n:",
                                      ["verbosity:", "number="])
    # Process parameters
    for o,p in opts:
        if o in ["-v", "--verbosity"]:
            pass # setDebug()
        if o in ["-n", "--number"]:
            n = int(p.strip("=:"))
    # find answer
    a = get_answer(n)
    print "Answer: %s" % a

if __name__ == "__main__":
    main()