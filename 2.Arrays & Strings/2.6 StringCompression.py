import unittest

#String compression: Implement a method to perform basic string compression using the counts of repeated characters. 
# For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller 
# than the original string, your method should return the original string. You can assume the string has only 
# uppercase and lowercase letters (a-z).

# Convert the string into an array and count each character until the next character is different. Then print 
# the character and the count. If the compressed string is longer than the original string return the original string.


class Solution:
    def stringCompression(self, s: str) -> str:
        compressed = []
        count = 0
        for i in range(len(s)):
            count += 1
            if i + 1 >= len(s) or s[i] != s[i + 1]:
                compressed.append(s[i])
                compressed.append(str(count))
                count = 0
        return min(s, ''.join(compressed), key=len)

class Test(unittest.TestCase):
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcd', 'abcd'),
        ('aaabbb', 'a3b3'),
        ('aabbcc', 'aabbcc')
    ]

    def test_stringCompression(self):
        solution = Solution()
        for test_string, expected in self.data:
            actual = solution.stringCompression(test_string)
            self.assertEqual(actual, expected, msg=f"Failed for: {test_string}")

if __name__ == "__main__":
    unittest.main()