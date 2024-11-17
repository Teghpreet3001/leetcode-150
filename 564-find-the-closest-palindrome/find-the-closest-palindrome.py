class Solution:

    def convert(self, num):
        s = str(num)
        n = len(s)
        left = (n - 1)//2
        right = n//2
        strList = list(s)
        while left >= 0:
            strList[right] = strList[left]
            right += 1
            left -= 1
        return int("".join(strList))

    def prevPalindrome(self, num):
        left = 0 
        right = num 
        res = float("-inf")
        while left <= right: 
            mid = (right - left) // 2 + left
            palin = self.convert(mid)
            if palin < num: 
                res = palin
                left = mid + 1
            else: 
                right = mid - 1
        return res 
        
    def nextPalindrome(self, num): 
        left= num 
        right = int(1e18)
        res = float("-inf")
        while left <= right: 
            mid = (right - left) //2 + left 
            palin = self.convert(mid)
            if palin > num:
                ans = palin 
                right = mid - 1
            else: 
                left = mid + 1
        return ans

    def nearestPalindromic(self, n: str) -> str:
        num = int(n)
        p1 = self.prevPalindrome(num)
        p2 = self.nextPalindrome(num)
        if abs(p1 - num) <= abs(p2 - num):
            return str(p1)
        return str(p2)