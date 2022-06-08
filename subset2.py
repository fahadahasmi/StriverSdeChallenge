class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        def helper(arr,op,ans,i):
            ans.append([j for j in op])
            
            for x in range(i,len(arr)):
                if x!=i and arr[x]==arr[x-1]:
                    continue
                
                op.append(arr[x])
                helper(arr,op,ans,x+1)
                op.pop()
        
        nums.sort()
        ans= []
        op = []
        helper(nums,op,ans,0)
        return ans
