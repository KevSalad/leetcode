# Two Hashing
# 1st Approach - Using built in functions with extra memory

"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for c in s:
            # check if function is alphanumerical 
            if c.isalnum():
                # make everything lowercase
                newStr += c.lower()
        # Automatically returns true or false 
        # [::-1] starts from the end
        return newStr == newStr[::-1]
"""

# 2nd Approach - Two Pointers

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialize left/right pointer
        l = 0
        r = len(s) - 1
        
        # While the pointers have not met
        while l < r:
            while l < r and not self.isAlphaNum(s[l]):
                l += 1
            while r > 1 and not self.isAlphaNum(s[r]):
                r -= 1
            # compare lowercases
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
    
    # Helper Function, if cannot use .isalnum()
    def isAlphaNum(self, c):
        # ord function allows us to get ASCII val
        # Checks if alphanumeric
        return (ord("A") <= ord(c) <= ord("Z") or 
                ord("a") <= ord(c) <= ord("z") or
                ord("0") <= ord(c) <= ord("9"))

