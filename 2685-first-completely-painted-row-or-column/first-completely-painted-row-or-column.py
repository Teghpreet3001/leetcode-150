class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:  
        # map each number in mat to its coordinates (row and column).
        cmap = {}
        n = len(mat)
        m = len(mat[0])

        for i in range(n):
            for j in range(m):
                val = mat[i][j]
                cmap[val] = (i,j)
        
        # rows[i] will keep track of how many elements in row i have been processed
        # cols[j] will keep track of how many elements in column j have been processed
        rows = [0]*n
        cols = [0]*m

        for i in range(len(arr)):
            #extract the coordinate in  the mat for the num in array

            rval = cmap[arr[i]][0] # 0 is x coordinate or rows
            rows[rval] += 1 

            cval = cmap[arr[i]][1] # 1 is x coordinate or rows
            cols[cval] += 1

            # r[d[arr[i]][0]] == m: This checks if the entire row has been processed (i.e., all m elements in the row have been marked).
            # c[d[arr[i]][1]] == n: This checks if the entire column has been processed (i.e., all n elements in the column have been marked).

            if  rows[rval] == m or cols[cval] == n:
                return i
        return -1
