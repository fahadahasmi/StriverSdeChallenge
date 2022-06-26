class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        def check(x,g,col):
            
            for i in g[x]:
                if col[i] == -1:
                    col[i] = 1 - col[x]
                    if not check(i,g,col):
                        return False

                elif col[i]==col[x]:
                    return False

            return True
        
        n = len(graph)
        col = [-1]*(n)
        
        g = graph
        for i in range(n):
            
            if col[i] == -1:
                col[i] = 1
                if not check(i,g,col):
                    return False
        return True
                
        
