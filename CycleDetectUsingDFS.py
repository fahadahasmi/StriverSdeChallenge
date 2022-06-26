from collections import deque
class Solution:
    
    #Function to detect cycle in an undirected graph.
    def isCycle(self, V, adj):
        #Code here
        
        def hasCycle(G,x,vis,par):
            vis[x] = True
            for i in G[x]:
                if not vis[i]:
                    if hasCycle(G,i,vis,x):
                        return True
                elif par != i:
                    return True
            return False
                        
        
        vis = [False]*(V)
        
        for i in range(V):
            
            if not vis[i]:
                if hasCycle(adj,i,vis,-1)==True:
                    return True
        
        return False

#{ 
#  Driver Code Starts
if __name__ == '__main__':

    T=int(input())
    for i in range(T):
        V, E = map(int, input().split())
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
        obj = Solution()
        ans = obj.isCycle(V, adj)
        if(ans):
            print("1")
        else:
            print("0")

# } Driver Code Ends
