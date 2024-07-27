class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        #We will keep two arrays to keep track of max product for positive numbers, and  min product fo negative numbers
        max_product = [1]*(n + 1)
        min_product = [1]*(n+1)

        max_product[0] = nums[0]
        min_product[0] = nums[0]
        result = nums[0]

        #every time. we encounter a negative number, we switch pn how to fill dp arary 
        for i in range(1, len(nums)):
            #for positive numbers, we can fill the array as it is 
            if nums[i] > 0:
                max_product[i] = max(nums[i], nums[i]*max_product[i-1])
                min_product[i] = min(nums[i], nums[i]*min_product[i-1])
            
            #for  negative numbers, we get  max product by mutiplying with the lowest number
            else:
                max_product[i] = max(nums[i], nums[i]*min_product[i-1])
                min_product[i] = min(nums[i], nums[i]*max_product[i-1])
            
            #updtae  result with  max_product
            result = max(result, max_product[i])
        return result