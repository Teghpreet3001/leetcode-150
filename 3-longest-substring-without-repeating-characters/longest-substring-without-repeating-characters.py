class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        result = 0

        for right in range(len(s)):
            for k in range(left, right):
                if s[k] == s[right]:
                    left = k + 1
                    break
            result = max(result, right - left + 1)
        
        return result
        

            
        