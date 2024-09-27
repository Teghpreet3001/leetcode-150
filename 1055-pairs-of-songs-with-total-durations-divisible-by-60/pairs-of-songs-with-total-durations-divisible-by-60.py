class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # move from O(n^2) solution to O(n) solution
        # if (a+b) % 60 = 0 then ((a % 60)+(b % 60)) % 60 
        # either (a % 60) == 0 or (b % 60) == 0 or (a+b) % 60 = 0
        
        '''
        res = 0
        for i in range(len(time)):
            for j in range(i + 1, len(time)):
                if i < j and (time[i] + time[j]) % 60 == 0:
                    res += 1
        return res
        '''
        modmap = collections.defaultdict(int) #maps numbers to their remainders: 0,1,2...58,59,60
        res = 0
        for num in time:
            if num % 60 == 0: # check if  b % 60 == 0
                res += modmap[0]
            else: #check for ((a % 60)+(b % 60)) = 60
                res += modmap[60 - (num % 60)]
            modmap[num % 60] += 1 #update for each number 
        return res 
