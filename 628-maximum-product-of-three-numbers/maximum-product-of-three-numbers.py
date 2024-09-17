class Solution:
    '''
    Sort the array: Sort the array in ascending order.

    Calculate products:

    Calculate the product of the three largest elements.
    Calculate the product of the two smallest elements and the largest element.
    Return the maximum: Return the larger of these two products.
    '''
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        prod1 = nums[-1]*nums[-2]*nums[-3]
        prod2 = nums[0]*nums[1]*nums[-1]
        return max(prod1, prod2)