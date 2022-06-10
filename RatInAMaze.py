#User function Template for python3

class Solution:
    def findPath(self, m, n):
        # code here
        
        def solve(arr,i,j,vis,ans,s,di,dj):
            if i==n-1 and j==n-1:
                ans.append(s)
                return
            
            direct = "DLRU"
            for x in range(4):
                nxti = i + di[x]
                nxtj = j + dj[x]
                
                if nxti >= 0 and nxtj >=0 and nxti<n and nxtj<n and vis[nxti][nxtj]!=1 and arr[nxti][nxtj]==1:
                    vis[i][j] = 1
                    solve(arr,nxti,nxtj,vis,ans,s+direct[x],di,dj)
                    vis[i][j] = 0
            
                
        vis = [[0 for x in range(n)]for y in range(n)]
        s = ""
        ans = []
        di = [+1,0,0,-1]
        dj = [0,-1,1,0]
        if m[0][0]==1:
            solve(m,0,0,vis,ans,s,di,dj)
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends
