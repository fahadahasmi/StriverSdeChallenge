class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
        def helper(ind,ans,arr):
            if ind==len(nums):
                ans.append([j for j in arr])
                return
            for i in range(ind,len(arr)):
                arr[ind],arr[i]=arr[i],arr[ind]
                helper(ind+1,ans,arr)
                arr[ind],arr[i]=arr[i],arr[ind]
        
        ans = []
        helper(0,ans,nums)
        return ans
