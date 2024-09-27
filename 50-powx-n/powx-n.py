class Solution:
    def myPow(self, x: float, n: int) -> float:
        return self.binaryExp(x, n)
    
    #time and space complexity: O(logn)
    def binaryExp(self, x, n): 
        if n == 0:
            return 1 
        # if raised to negative number, we get the positive result and take the reciprocal of it
        if n < 0:
            return 1.0 / self.binaryExp(x, n * -1)

        # if n is odd, we perform binary exponentiation to reduce the number of steps logarithmically on n - 1 and multiply  by x
        # otherwise we calculate the result on n
        if n % 2 == 1:
            return x * self.binaryExp(x*x, (n-1)//2)
        
        else:
            return self.binaryExp(x*x, n//2)
