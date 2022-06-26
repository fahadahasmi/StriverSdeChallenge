def check(node,g,vis,dv):
    vis[node] = 1
    dv[node] = 1
    for i in g[node]:
        if not vis[i]:
            if check(i,g,vis,dv):
                return True
        elif dv[i]:
            return True
    dv[node] = 0
    return False

def detectCycleInDirectedGraph(n, edges):
    # Write your code here
    g = [[] for _ in range(n+1)]
    
    for x,y in edges:
        g[x].append(y)
        
    vis = [0]*(n+1)
    dfsVis = [0]*(n+1)
    for i in range(1,n+1):
        
        if not vis[i]:
            if check(i,g,vis,dfsVis):
                return True
    return False
