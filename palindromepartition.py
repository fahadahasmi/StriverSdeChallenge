class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isPal(a,i,j):
            
            while i<=j:
                if a[i]!=a[j]:
                    return False
                i+=1
                j-=1
            return True
        
        def helper(st,op,ans,i):
            
            if i==len(st):
                ans.append([j for j in op])
                print(op)
                return
            
            for x in range(i,len(st)):
                
                if isPal(st,i,x):
                    op.append(st[i:x+1])
                    helper(st,op,ans,x+1)
                    op.pop()
        
        ans = []
        op = []
        
        helper(s,op,ans,0)
        return ans
