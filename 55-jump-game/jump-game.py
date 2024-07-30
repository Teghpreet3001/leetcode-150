class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
        '''
        maxJump = 0
        goal = len(nums) - 1
        for i in range(goal + 1):
            if i > maxJump:
                return False
            maxJump = max(maxJump, i + nums[i])
        return True