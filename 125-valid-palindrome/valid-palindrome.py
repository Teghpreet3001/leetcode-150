class Solution(object):
    def isPalindrome(self, word):
        """
        :type s: str
        :rtype: bool
        """
        s = ''
        for char in word:
            if char.isalnum():
                s += char.lower()
        print(s)
        low = 0 
        high = len(s) - 1
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else: 
                return False
        return True