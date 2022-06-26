from collections import deque
class Solution:
    
    #Function to detect cycle in an undirected graph.
    def isCycle(self, V, adj):
        #Code here
        
        def isCycle(G,x,vis):
            vis[x] = True
            q = deque()
            q.append(x)
            par = [-1]*(V)
            
            while q:
                node = q.pop()
                
                for i in G[node]:
                    if not vis[i]:
                        vis[i] = True
                        q.append(i)
                        par[i] = node
                    elif par[node] != i:
                        return True
            return False
                        
        
        vis = [False]*(V)
        
        for i in range(V):
            
            if not vis[i]:
                if isCycle(adj,i,vis):
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
