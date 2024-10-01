class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = 0
        result = 0

        #there are k mod groups 0...k-1
        #dp[R] = number of subarrays encountered with remainder R ewhen divided by k
        dp = [0]*k
        dp[0]  = 1

        for num in nums:
            #take modulo twice to avoid negative numbers
            prefix = (prefix + num % k + k) % k
            #append count to the result
            result += dp[prefix]
            dp[prefix] += 1
        return result