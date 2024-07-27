class Solution:

    def numDecodings(self, s: str) -> int:
        #bottom up dp
        n = len(s)
        #dp is a 1D array that stores num ways for a string of dp[i:]
        #since it is bottom up, we start loop backwards and return dp[0]
        dp1 = 1
        dp2 = 0

        for i in range(len(s)-1, -1, -1):
            #base case that the string starts with 0
            if s[i] == "0":
                dp = 0
            else: #string is btw 0 to 9 so we add the next one digit 
                dp = dp1
            
            #check if the next two digits are valid and add them
            #only going to be valid  if starts with 1 or 2 and  second digot is 0,1,2,3,4,5,6 (only for 2) as 26 is the  max value 
            #for example, 31 is not valid so we do not add that 
            # To make sure taht we do not run into index out of range, we chcek if i+1 < len(s)

            if (i + 1 < len(s)) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                dp += dp2
            dp2 = dp1
            dp1 = dp

        print(dp)
        return dp