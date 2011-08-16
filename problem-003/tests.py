"""
Unit tests for solution
"""

import unittest
import solution

class KnownValues(unittest.TestCase):
    knownValues = ((1, True),
                   (2, False),
                   (3, True),
                   (4, False),
                   (5, True),
                   (6, False),
                   (7, True),
                   (8, False),
                   (9, False),
                   (10, False),
                   (13, True),
                   (29, True))

    def test_is_prime(self):
        """is_prime should return true for known values"""
        for number, is_prime in self.knownValues:
            self.assertEqual(solution.is_prime(number), is_prime)
            
if __name__ == "__main__":
    unittest.main()