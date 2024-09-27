class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        if startValue*2 == target or startValue-1 == target:
            return 1 
        res = 0
        #we greedily divide by 2: add 1 if it is odd or divide by 2 if its even until we move towards the startValue
        # answer is res + startValue - target
        while target > startValue:
            res += 1
            if target % 2 == 1:
                target += 1
            else:
                target //= 2
        return res + startValue - target