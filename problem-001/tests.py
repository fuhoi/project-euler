"""
Unit tests for solution
"""

import unittest
import solution

class KnownValues(unittest.TestCase):
    knownValues = ((10, [1,2,3,4,5,6,7,8,9], [3,5], [3,5,6,9], 23),
                   (10, [1,2,3,4,5,6,7,8,9], [1], [1,2,3,4,5,6,7,8,9], 45),
                   (10, [1,2,3,4,5,6,7,8,9], [2], [2,4,6,8], 20),
                   (10, [1,2,3,4,5,6,7,8,9], [3], [3,6,9], 18),
                   (10, [1,2,3,4,5,6,7,8,9], [1,2], [1,2,3,4,5,6,7,8,9], 45),
                   (10, [1,2,3,4,5,6,7,8,9], [2,3], [2,3,4,6,8,9], 32))

    def test_multiples(self):
        """Multiples should return a list of multiples"""
        for limit, numerators, denominators, multiples, total in self.knownValues:
            result = solution.get_multiples(numerators, denominators)
            result.sort()
            self.assertEqual(result, multiples)

    def test_total(self):
        """Total should return the total of multiples"""
        for limit, numerators, denominators, multiples, total in self.knownValues:
            result = solution.get_total(multiples)
            self.assertEqual(result, total)
            
    def test_answer(self):
        """Answer should return answer"""
        for limit, numerators, denominators, multiples, total in self.knownValues:
            result = solution.get_answer(limit, denominators)
            self.assertEqual(result, total)
            
if __name__ == "__main__":
    unittest.main()