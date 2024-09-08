import unittest

# There are theree types of edits that can be performed on strings: insert a character, remove a character, 
# or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.

# EXAMPLE 
# pale, ple -> true 
# pales, pale -> true 
# pale, bale -> true  
# pale, bake -> flase


#If the length of the strings are the same then only 1 char can be replaced
#If the length of the strings are different then only 1 char can be inserted or removed
#Nothing was edited 


def oneAway(s1, s2):
    if len(s1) == len(s2):
        return oneEditReplace(s1, s2)
    elif len(s1) + 1 == len(s2):
        return oneEditInsert(s1, s2)
    elif len(s1) - 1 == len(s2):
        return oneEditInsert(s2, s1)
    return False
    
def oneEditReplace(s1,s2):
    edited = False
    for t1, t2 in zip(s1,s2):
        if t1 != t2:
            if edited: 
                return False
            edited = True
    return True

def oneEditInsert(s1,s2):
    edited = False 
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if edited:
                return False
            edited = True
            j += 1
        else:
            i += 1
            j += 1
    return True


class Test(unittest.TestCase):
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = oneAway(test_s1, test_s2)
            self.assertEqual(actual, expected, msg=f"Failed for: {test_s1,test_s2} Expected Output: {expected}")
        
    
if __name__ == "__main__":
    unittest.main()