class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        op = []
        
        
        def helper(arr,i,sum,op,ans):
            
            if i>=len(arr):
                if sum==0:
                    ans.append([x for x in op])
                return
            
            if arr[i] <= sum:
                op.append(arr[i])
                helper(arr,i,sum-arr[i],op,ans)
                op.pop()
            
            helper(arr,i+1,sum,op,ans)
            
        helper(candidates,0,target,op,ans)
        return ans
            
