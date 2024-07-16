class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #double for loop where we compute the window and compare every element in the window with right 
        '''
        left = 0
        result = 0

        for right in range(n):
            for k in range(left, right):
                if s[k] == s[right]:
                    left = k + 1
                    break
            result = max(result, right - left + 1)
        
        return result
        '''
        #essentially checking if right and left chars are both in the same  since they are same. If they are, we remove the left one and move it  one forward
        left = 0
        right = 0 #both start at 0 since we want them to same for  first iteration
        result = 0
        charSet =  set() #basucally holds the chars of the longest non repeating substring
        while right < len(s):
            while s[right] in charSet:
                charSet.remove(s[left]) #remove the last char
                left += 1
            charSet.add(s[right]) #add the next char
            result = max(result, right - left + 1) #checking with size of window
            right += 1
        return result

            
        