# [Problem 2](http://projecteuler.net/index.php?section=problems&id=2)

## Overview

### Description

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

### Solution

Unanswered

## Getting Started

### How to run

    python solution.py -l=4000000

Or:

    python solution.py --limit=4000000

### Supported flags

* `-v, --verbose` - verbose output (0=CRITICAL, 1=ERROR, 2=WARN, 3=INFO, 4=DEBUG)
* `-l, --limit` - upper limit

## Requirements

### Definitions

* Fibonacci sequence - generated by adding the previous two terms
* Even - divisible by two (no remainder)

### Observations

* The first ten terms of the Fibonacci sequence beginning with 1 and 2 are 1, 2, 3, 5, 8, 13, 21, 34, 55 and 89
* Must sum the even values
* Sequence contains unique list of numbers (no duplicates)

### Test cases

* The first ten terms of the Fibonacci sequence beginning with 1 and 2 are 1, 2, 3, 5, 8, 13, 21, 34, 55 and 89. The even terms are 2, 8 and 34. Their sum is 44.

## Design

### Initial design

* `fib(i, j)` - returns the next number in the Fibonacci sequence