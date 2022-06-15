class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        h = len(nums)-2
        
        while l<=h:
            
            mid = (l+h)//2
            
            if mid%2!=0:
                
                if nums[mid]==nums[mid+1]:
                    h = mid-1
                else:
                    l = mid+1
            else:
                
                if nums[mid] != nums[mid+1]:
                    h = mid -1 
                else:
                    l =mid+1
        
        return nums[l]
                    
