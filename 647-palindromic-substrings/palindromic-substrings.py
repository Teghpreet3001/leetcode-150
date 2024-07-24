class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        #P[i][j] = whether or not i to j is a palindrome 
        P = [[False for i in range(len(s))] for j in range(len(s))]
        n = len(s)
        result = 0

        #minimum palindromic strings in a singe char is 1
        for i in range(len(s)):
            P[i][i] = True
            result += 1

        # Check for two character substrings
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                P[i][i + 1] = True
                result += 1

        # Check for substrings of length 3 or more
        for length in range(3, n + 1):  # length is the length of the substring
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and P[i + 1][j - 1]:
                    P[i][j] = True
                    result += 1
        return result
