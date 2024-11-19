from collections import deque
class Solution:
    # Idea is that we do not need to check the difference between all the elements, only the the smallest and the largest
    # We use sliding window approach 
    # We can use minheap, maxheap but that will lead to time complextity of O(nlogn) so we use two deques: min_deque and max_deque
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        max_deque = deque()
        min_deque = deque()
        left = 0
        max_length = 0 
        
        for right in range(len(nums)): 
            while max_deque and max_deque[-1] < nums[right]:
                max_deque.pop()
            max_deque.append(nums[right])

            while min_deque and min_deque[-1] > nums[right]:
                min_deque.pop()
            min_deque.append(nums[right])

            while max_deque[0] - min_deque[0] > limit: 
                if max_deque[0] == nums[left]:
                    max_deque.popleft()
                if min_deque[0] == nums[left]:
                    min_deque.popleft()
                left += 1
            curr_window_length = right - left + 1
            max_length = max(max_length, curr_window_length)
        return max_length