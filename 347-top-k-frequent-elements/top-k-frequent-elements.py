class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        map = {}
        for num in nums:
            if num not in map:
                map[num] = 1
            else:
                map[num] += 1
        res = []
        for num, count in map.items():
            res.append((num, count))
        print(map)
        res_sorted = sorted(res, key=lambda x: x[1], reverse=True)
        print(res_sorted)
        parts = res_sorted[:k]
        result = []
        for part in parts:
            result.append(part[0])
        return result

        