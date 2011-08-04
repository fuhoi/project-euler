[Problem 1](http://projecteuler.net/index.php?section=problems&id=1)
=

Description
-
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

Design
-
remainder(numerator, denominator) - returns the remainder of the numerator divided by the denominator

isDivisor(numerator, denominator) - returns true if remainder(numerator, denominator) is zero

multiples(numerators, denominators) - returns a list of numerators where isDivisor is true