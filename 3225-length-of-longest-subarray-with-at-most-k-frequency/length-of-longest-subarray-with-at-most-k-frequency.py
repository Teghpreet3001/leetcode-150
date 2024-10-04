from collections import Counter
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        res = 0 
        left = 0
        right = 0
        freq = Counter()
        
        while right  < len(nums):
            freq[nums[right]] += 1

            #check if the condition for good becomes false
            while freq[nums[right]] > k: 
                freq[nums[left]] -= 1
                left += 1 #move left to next subarray
                 
            res = max(res, right - left + 1)
            right += 1
        return res  