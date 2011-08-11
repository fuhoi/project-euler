# [Problem 1](http://projecteuler.net/index.php?section=problems&id=1)

## Description
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

## Definitions
* Natural number - integer or whole number (in this case excluding zero)
* Multiple - the product of two natural numbers

## Observations
* Range of candidates begins at 1
* Range of candidates ends 1 number before the limit (with limit of 10, last number in range is 9)
* Sequence contains all numbers between beginning and end that is divisible by the denominators
* Sequence contains unique list of numbers (no duplicates)

## Test cases
* Sequence with a range beginning at 1 and ending at 10 with a denominator of 3 and 5 would contain 3, 5, 6 and 9 with a total of 23
* Sequence with a range beginning at 1 and ending at 10 with a denominator of 1 would contain 1, 2, 3, 4, 5, 6, 7, 8 and 9 with a total of 45
* Sequence with a range beginning at 1 and ending at 10 with a denominator of 2 would contain 2, 4, 6 and 8 with a total of 20
* Sequence with a range beginning at 1 and ending at 10 with a denominator of 1 and 2 would contain 1, 2, 3, 4, 5, 6, 7, 8 and 9 with a total of 45
* Sequence with a range beginning at 1 and ending at 10 with a denominator of 3 would contain 3, 6 and 9 with a total of 18
* Sequence with a range beginning at 1 and ending at 10 with a denominator of 2 and 3 would contain 2, 3, 4, 6, 8 and 9 with a total of 32

## Design
### Current design
* `remainder(numerator, denominator)` - returns the remainder of the numerator divided by the denominator
* `isDivisor(numerator, denominator)` - returns true if remainder(numerator, denominator) is zero
* `multiples(numerators, denominators)` - returns a list of numerators where isDivisor is true

## Getting Started
### How to run
    python solution.py -n=1000 -d=3,5

Or:

    python solution.py --limit=1000 --denominators=3,5

### Supported flags
* `-D, --debug` - verbose output
* `-n, --limit` - upper limit
* `-d, --denominators` - denominators

## Solution
The answer to this problem is 233168