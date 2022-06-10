#User function Template for python3


#Function to determine if graph can be coloured with at most M colours such
#that no two adjacent vertices of graph are coloured with same colour.
def graphColoring(graph, k, V):
    
    def isSafe(g,color,node,n,col):
        for k in range(n):
            if k!=node and g[k][node]==1 and color[k]==col:
                return False
        return True
    
    def solve(g,i,color,m,n):
        if i==n:
            return 1
        
        for x in range(1,m+1):
            if isSafe(g,color,i,n,x):
                color[i] = x 
                if solve(g,i+1,color,m,n)==1:
                    return 1
                color[i] = 0
        
        return 0
        
    
    n = len(graph)
    color = [0]*(n)
    
    if solve(graph,0,color,k,n)==1:
        return 1
    return 0
    
    #your code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        V = int(input())
        k = int(input())
        m = int(input())
        list = [int(x) for x in input().strip().split()]
        graph = [[0 for i in range(V)] for j in range(V)]
        cnt = 0
        for i in range(m):
            graph[list[cnt]-1][list[cnt+1]-1]=1
            graph[list[cnt+1]-1][list[cnt]-1]=1
            cnt+=2
        if(graphColoring(graph, k, V)==True):
            print(1)
        else:
            print(0)

        t = t-1

# } Driver Code Ends
