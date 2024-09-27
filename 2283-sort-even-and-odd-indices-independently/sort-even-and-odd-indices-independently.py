class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        res1 = [] #even
        res2 = [] #odd
        for i in range(len(nums)):
            if i % 2 == 0:
                res1.append(nums[i])
            else:
                res2.append(nums[i])
        res1.sort()
        res2.sort(reverse = True)
        return self.merge(res1, res2)
    
    def merge(self, list1: List[int], list2: List[int]) -> List[int]:
        merged_list = []
        max_len = max(len(list1), len(list2))
        for i in range(max_len):
            if i < len(list1):
                merged_list.append(list1[i])
            if i < len(list2):
                merged_list.append(list2[i])
        return merged_list



