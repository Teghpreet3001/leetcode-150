class Solution:
    def intToRoman(self, num: int) -> str:
        num_map = {
            1: "I",
            5: "V",    4: "IV",
            10: "X",   9: "IX",
            50: "L",   40: "XL",
            100: "C",  90: "XC",
            500: "D",  400: "CD",
            1000: "M", 900: "CM",
        }
        res = ""
        #start and subtract the highest value
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        for n in nums:
            while n <= num:
                res += num_map[n]
                #print(res)
                num -= n
        return res 