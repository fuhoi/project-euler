"""
Project Euler problem 3 solution
"""

__version__ = "$Revision: 1.0 $"
# $Source$

__author__ = "Adam Lincoln (adam.k.lincoln@gmail.com)"
__date__ = "$Date: 2011/08/015 $"

import functools
import getopt
import logging
import math
import sys
import time

# create logger with 'solution'
logger = logging.getLogger('solution')
logger.setLevel(logging.INFO)
# create file handler which logs even debug messages
fh = logging.FileHandler('solution.log')
fh.setLevel(logging.INFO)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)
    
def log(func):
    """Print function details."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        #logger.info("%s %s", (func.__name__, ", ".join(args)))
        #print func.__name__, args, kwargs
        res = func(*args, **kwargs)
        return res
    return wrapper

def benchmark(func):
    """Print function execution time."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print func.__name__, time.clock()-t
        return res
    return wrapper

def counter(func):
    """Print execution count of function."""
    counter.count = 0
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        counter.count = counter.count + 1
        res = func(*args, **kwargs)
        print func.__name__, "has been used : ", counter.count, "X"
        return res
    return wrapper

def is_prime(n):
    """Return true if number is prime"""
    # even is not prime
    # NOTE: Do not even process even numbers fool
    #if n % 2 == 0:
        #print "%s is not prime" % n
    #    return False
    # everything is divisible by 1 so don't test that
    # we just tested 2 so start at 3
    # n is not going to be divisible after floor(n / 2) so end there (don't waste time after that)
    for d in range(3, int(math.floor(n / 2)), 2):
        #print "denominator: %s" % d
        if n % d == 0:
            #print "%s is not a prime" % n
            return False # Number is divisible, not prime
    else: # No divisors
        #print "%s is a prime" % n
        return True # Prime!
    return False # Shouldn't get here
    
@counter
@benchmark
@log  
def get_answer(number):
    """Return solution answer."""
    
    # Initialise
    f = [] # Factors
    i = 3 # Start
    max = int(math.floor(number / 2)) # Max divisor
    
    # Parameters
    logger.info("get_answer - Number: %s" % number)
    logger.info("get_answer - f: %s" % f)
    logger.info("get_answer - i: %s" % i)
    logger.info("get_answer - max: %s" % max)
    
    # Main loop
    while i < max:
    
        logger.info("get_answer - Current: %s" % i)
        
        if number % i == 0: # Divisor
        
            logger.info("get_answer - %s divides %s, is it prime?" % (i, number))
            
            j = 3
            m = int(math.floor(i / 2))
            
            while j < m:
                if i % j == 0:
                    break
                j += 2
                if j % 5 == 0 and j > 5: # Skip numbers ending in 5
                    j += 2
            else:
                f.append(i)
        
            #if is_prime(i): # Prime
                #logger.info("get_answer - %s is prime" % i)
                #f.append(i)
                
        i += 2 # Do not include even numbers
        
        if i % 5 == 0 and i > 5: # Skip numbers ending in 5
            i += 2
        
    logger.info("List %s" % f)
    logger.info("Largest: %s" % f[-1:])
    
    return sum(f[-1:])

def main():
    # Default values
    logger.info('setting default values')
    n = 13195
    # Parse parameters
    logger.info('parsing parameters')
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
    logger.info('calling get answer(' + str(n) + ')')
    a = get_answer(n)
    print "Answer: %s" % a

if __name__ == "__main__":
    main()