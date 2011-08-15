"""
Unit tests for solution
"""

import unittest
import solution

class KnownValues(unittest.TestCase):
    knownValues = ((1, true),
                   (2, true),
                   (3, true),
                   (4, true),
                   (5, true),
                   (6, true),
                   (7, true),
                   (8, true),
                   (9, true),
                   (10, true))

    # def test_multiples(self):
        # """Multiples should return a list of multiples"""
        # for limit, numerators, denominators, multiples, total in self.knownValues:
            # result = solution.get_multiples(numerators, denominators)
            # result.sort()
            # self.assertEqual(result, multiples)

    # def test_total(self):
        # """Total should return the total of multiples"""
        # for limit, numerators, denominators, multiples, total in self.knownValues:
            # result = solution.get_total(multiples)
            # self.assertEqual(result, total)
            
    # def test_answer(self):
        # """Answer should return answer"""
        # for limit, numerators, denominators, multiples, total in self.knownValues:
            # result = solution.get_answer(limit, denominators)
            # self.assertEqual(result, total)

    def test_is_prime(self):
        """is_prime should return true for known values"""
        self.assertEqual(is_prime(1), true)
        self.assertEqual(is_prime(2), true)
        self.assertEqual(is_prime(3), true)
        self.assertEqual(is_prime(4), true)
        self.assertEqual(is_prime(5), true)
        self.assertEqual(is_prime(6), true)
        self.assertEqual(is_prime(7), true)
        self.assertEqual(is_prime(8), true)
        self.assertEqual(is_prime(9), true)
        self.assertEqual(is_prime(10), true)
            
if __name__ == "__main__":
    unittest.main()