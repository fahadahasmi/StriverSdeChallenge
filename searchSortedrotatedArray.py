class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l,h  = 0,len(nums)-1
        
        while l<=h:
            mid = (l+h)//2
            
            if nums[mid]==target:
                return mid
            
            if nums[mid] >= nums[l]:
                if nums[l] <= target and nums[mid] >= target:
                    h = mid-1
                else:
                    l = mid+1
            else:
                if nums[h]>=target and nums[mid] <= target:
                    l =mid+1
                else:
                    h = mid-1
        
        return -1
