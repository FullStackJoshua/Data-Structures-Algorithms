import unittest

# URLify: Write a method to replace all spaces in a string with '%20'. 
# You may assume that the string has sufficient space at the end to hold the additional characters, 
# and that you are given the "true" length of the string.

# class Solution: 
#     def URLify1(self, s: str) -> str:
#         return s.replace(' ', '%20')

class Solution:
    def URLify(self, s: str, length: int) -> str:
        s = list(s)
        new_index = len(s)

        for i in reversed(range(length)):
            if s[i] == ' ':
                s[new_index - 3:new_index] = '%20'
                new_index -= 3
            else:
                s[new_index - 1] = s[i]
                new_index -= 1

        return ''.join(s)
         

class Test(unittest.TestCase):
    data = [
        ('Mr John Smith    ', 13, 'Mr%20John%20Smith')
    ]

    def test_URLify(self):
        solution = Solution()
        for test_string, length, expected in self.data:
            actual = solution.URLify(test_string, length)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()