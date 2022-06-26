class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(g,i,j):
            
            if i<0 or j<0 or j>=len(g[0]) or i>=len(g) or g[i][j] != "1":
                return 
            g[i][j] = "*"
            
            dfs(g,i-1,j)
            dfs(g,i+1,j)
            dfs(g,i,j-1)
            dfs(g,i,j+1)
        
        if not grid:
            return 0
        
        c = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == '1':
                    dfs(grid,i,j)
                    c+=1 
        return c
