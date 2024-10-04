class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        # count the number of zeros in each array and add them up with the sums respectively.

        counter1 = Counter(nums1)
        zerocount1 = counter1[0]

        counter2 = Counter(nums2)
        zerocount2 = counter2[0]

        sum1 = sum(nums1)
        sum2 = sum(nums2)

        sum1 += zerocount1
        sum2 += zerocount2

        #the only impossible case is when there are no zeroes in one array and the sum of the other  array is greater, meaning we ve to incease the sum of array 1 but without any zeroes which is impossible 
        if (zerocount1 == 0 and sum2 > sum1) or (zerocount2 == 0 and sum1 > sum2):
            return -1
        #else return the max of the sum which is guaranttted to be  made  by substituting the zeroes. 
        return max(sum1, sum2)



