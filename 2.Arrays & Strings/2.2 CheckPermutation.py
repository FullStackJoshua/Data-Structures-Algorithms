import unittest

#Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

class Solution:
    def checkPermutation (self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        return sorted(s1) == sorted(s2)


class Test(unittest.TestCase):
    dataT = [('abcd', 'bacd'), ('3563476', '7334566'), ('wef34f', 'wffe34')]
    dataF = [('abcd', 'd2cba'), ('2354', '1234'), ('dcw4f', 'dcw5f'), ('do g', 'dog'), ('cat', 'Cat')]

    def test_check_permutation(self):
        solution = Solution()
        # true check
        for s1, s2 in self.dataT:
            actual = solution.checkPermutation(s1, s2)
            self.assertTrue(actual, msg=f"Failed for: {s1}, {s2}")
        # false check
        for s1, s2 in self.dataF:
            actual = solution.checkPermutation(s1, s2)
            self.assertFalse(actual, msg=f"Failed for: {s1}, {s2}")

if __name__ == "__main__":
    unittest.main()