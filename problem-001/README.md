# [Problem 1](http://projecteuler.net/index.php?section=problems&id=1)

## Overview

### Description

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

### Solution

The answer to this problem is 233168

## Getting Started

### How to run

    python solution.py -l=1000 -d=3,5

Or:

    python solution.py --limit=1000 --denominators=3,5 --verbosity=0

### Supported flags

* `-v, --verbose` - verbose output (0=CRITICAL, 1=ERROR, 2=WARN, 3=INFO, 4=DEBUG)
* `-l, --limit` - upper limit
* `-d, --denominators` - denominators

## Requirements

### Definitions

* Natural number - integer or whole number (in this case excluding zero)
* Multiple - the product of two natural numbers

### Observations

* Range of integers begins at 1
* Range of integers ends 1 number before the limit (with limit of 10, last number in range is 9) [f^(n-1)]
* Sequence contains all numbers between beginning and end that is divisible by the denominators
* Sequence contains unique list of numbers (no duplicates)

### Test cases

* Sequence with a range beginning at 1 and ending at 10 with a denominator of 3 and 5 would contain 3, 5, 6 and 9 with a total of 23
* Sequence with a range beginning at 1 and ending at 10 with a denominator of 1 would contain 1, 2, 3, 4, 5, 6, 7, 8 and 9 with a total of 45
* Sequence with a range beginning at 1 and ending at 10 with a denominator of 2 would contain 2, 4, 6 and 8 with a total of 20
* Sequence with a range beginning at 1 and ending at 10 with a denominator of 1 and 2 would contain 1, 2, 3, 4, 5, 6, 7, 8 and 9 with a total of 45
* Sequence with a range beginning at 1 and ending at 10 with a denominator of 3 would contain 3, 6 and 9 with a total of 18
* Sequence with a range beginning at 1 and ending at 10 with a denominator of 2 and 3 would contain 2, 3, 4, 6, 8 and 9 with a total of 32

## Design

### Second revision

* `main()` - process script parameters and display answer
* `get_answer(limit, denominators)` - return solution answer
* `get_multiples(numerators, denominators)` - return list of numerators divisible by list of denominators
* `get_numerators(limit)` - return numbers between 1 and limit (exclusive, or limit-1)
* `get_total(multiples)` - return total of multiples
* `is_divisor(numerator, denominator)` - return true if remainder of division is zero

### First revision

* `get_numerators(min, max)` - return numbers between min (inclusive) and max (exclusive, or max-1)
* `get_multiples(numerators, denominators)` - return list of numerators divisible by list of denominators
* `is_divisor(numerator, denominator)` - return true if remainder of division is zero
* `get_remainder(numerator, denominator)` - return remainder of numerator divided by denominator
* `get_total(multiples)` - return total of multiples
* `get_answer(min, max, denominators)` - return solution answer
* `main()` - process script parameters and display answer

#### Performance

* `is_divisor` is still called for each denominator

### Initial design

* `remainder(numerator, denominator)` - returns the remainder of the numerator divided by the denominator
* `isDivisor(numerator, denominator)` - returns true if remainder(numerator, denominator) is zero
* `multiples(numerators, denominators)` - returns a list of numerators where isDivisor is true

#### Performance

* `is_divisor` is called for each denominator