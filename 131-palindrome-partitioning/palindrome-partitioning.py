class Solution(object):
    def palindrome(self, s, start, end):
        if start > end:
            return False
        if start == end:
            return True
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    def backtrack(self, result, partition, s, start):
        #we have checked all possibele partitions
        if start == len(s):
            result.append(list(partition))
        for i in range(start, len(s)):
            if not self.palindrome(s, start, i):
                continue
            partition.append(s[start:i+1])
            self.backtrack(result, partition, s, i + 1)
            partition.pop()

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        partition = []
        self.backtrack(result, partition, s, 0)
        return result