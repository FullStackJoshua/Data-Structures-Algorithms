import unittest

# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

class Solution:
    def isUnique(self, s: str) -> bool:
        # Assuming the string is ASCII (128 characters)
        if len(s) > 128:
            return False
        char_set = [False for _ in range(128)]
        for char in s:
            val = ord(char)
            if char_set[val]:
                return False
            char_set[val] = True
        return True


class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        solution = Solution()
        # true check
        for test_string in self.dataT:
            actual = solution.isUnique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = solution.isUnique(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()