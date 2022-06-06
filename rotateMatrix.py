class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        ans = [[0* x for x in range(n)]for m in range(m)]
        
        for i in range(m):
            for j in range(n):
                
                ans[j][i] = matrix[i][j]
                
        
        for i in range(m):
            ans[i].reverse()
        
        for i in range(m):
            for j in range(n):
                matrix[i][j] = ans[i][j]
