# [Problem 3](http://projecteuler.net/index.php?section=problems&id=3)

## Overview

### Description

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

### Solution

Unanswered

## Getting Started

### How to run

```shell
python solution.py -n=13195
```

Or:

```shell
python solution.py --number=600851475143
```

### Supported flags

* `-v, --verbose` - verbose output (0=CRITICAL, 1=ERROR, 2=WARN, 3=INFO, 4=DEBUG)
* `-n, --number` - number

## Requirements

### Definitions

* Prime number
* Factor

### Observations

* The prime factors of 13195 are 5, 7, 13 and 29. The largest being 29.
* Must find the largest
* Start at the floor of half the number and work in descending order to three.

### Test cases

* The prime factors of 13195 are 5, 7, 13 and 29. The largest being 29.

## Design

### Initial design

* `is_prime(n)` - return true if n is prime
* `is_factor(n, d)` - return true if d is a factor of n
* `find_largest_prime_factor(n)` - return largest prime factor