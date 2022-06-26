from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        def check(x,g,col,n):
            
            q = deque()
            q.append(x)
            col[x] = 1
            while q:
                node = q.pop()
                for i in g[node]:
                    if col[i] == -1:
                        col[i] = 1 - col[node]
                        q.append(i)
                        
                    elif col[i]==col[node]:
                        return False

            return True
        
        n = len(graph)
        col = [-1]*(n)
        
        g = graph
        for i in range(n):
            
            if col[i] == -1:
                if not check(i,g,col,n):
                    return False
        return True
                
        
