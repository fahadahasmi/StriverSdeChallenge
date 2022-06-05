class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n):
            if i!=0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,n):
                if j != i+1 and nums[j]==nums[j-1]:
                    continue
                l = j+1
                h = n-1
                while l<h:
                    s = nums[i]+nums[j]+nums[l]+nums[h]
                    
                    if s < target:
                        l+=1
                    elif s > target:
                        h-=1
                    else:
                        ans.append([nums[i],nums[j],nums[l],nums[h]])
                        while l<h and nums[l] == nums[l+1]:
                            l+=1
                        while l<h and nums[h] == nums[h-1]:
                            h-=1
                        l+=1
                        h-=1
        return ans
