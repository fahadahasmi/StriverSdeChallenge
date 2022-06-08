class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        op = []
        
        candidates.sort()
        
        def helper(arr,i,op,ans,sum):
            
            if sum==0:
                ans.append([y for y in op])
                return
            
            for x in range(i,len(arr)):
                
                if x>i and arr[x] == arr[x-1]:
                    continue
                
                if arr[x]<=sum:
                    op.append(arr[x])
                    helper(arr,x+1,op,ans,sum-arr[x])
                    op.pop()
                else:
                    break
        
        helper(candidates,0,op,ans,target)
        return ans
