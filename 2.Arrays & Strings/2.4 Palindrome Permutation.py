import unittest
import collections
# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. 
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. 
# The palindrome does not need to be limited to just dictionary words.

# Permuations: Can be written in mutiple ways.
# Palindrome: Can be spelled forwards and backwards the same way.

     
# Even number of strings of must have even number of characters.
# Odd number of strings must have 1 odd charcater and the rest must be even 


class Solution:
    def palindromePermutation(self, s: str) -> bool:
        count = collections.Counter(s)
        counter = 0  # If this ends with 1 after looping through the key value pair it is a palindrome (True). 
                     # If the count is even then counter will remain 0 (True). 
                     # If it's greater than 1 return (False).
        
        for key in count:
            counter += count[key] % 2
    
        if counter == 1 or counter == 0:
            return True
        else:
            return False


class Test(unittest.TestCase):
    dataT = [('aab')]
    dataF = [('abc')]

    def test_palindromePermutation(self):
        solution = Solution()
        # true check
        for s in self.dataT:
            actual = solution.palindromePermutation(s)
            self.assertTrue(actual, msg=f"Failed for: {s}")
        # false check
        for s in self.dataF:
            actual = solution.palindromePermutation(s)
            self.assertFalse(actual, msg=f"Failed for: {s}")

if __name__ == "__main__":
    unittest.main()


     
    






