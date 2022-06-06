class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ans = []
        i=j=0
        
        while i<m and j<n:
            if nums1[i] < nums2[j]:
                ans.append(nums2[j])
                j+=1
            else:
                ans.append(nums1[i])
                i+=1
        
        while i<m:
            ans.append(nums1[i])
            i+=1
        
        while j<n:
            ans.append(nums2[j])
            j+=1
        
        ans.sort()
        
        for c in range(len(nums1)):
            nums1[c] = ans[c]
        
        
