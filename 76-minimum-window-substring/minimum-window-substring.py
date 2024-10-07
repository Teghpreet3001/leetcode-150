from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) == 0 or len(t) == 0 or len(s) < len(t):
            return ""
        map = Counter(t)   
        count  = len(t)
        start = 0
        end = 0
        minlength = float("inf")
        startIndex  = 0 
        
        while end < len(s):
            if map[s[end]] > 0:
                count -= 1
            map[s[end]] -= 1
            end += 1

            while count == 0:
                if end - start < minlength:
                    minlength = end - start
                    startIndex = start
                if map[s[start]] == 0:
                    count += 1
                map[s[start]] += 1
                start  += 1
        
        if minlength == float("inf"):
            return ""
        else:
            return s[startIndex: startIndex + minlength]