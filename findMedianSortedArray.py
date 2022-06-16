class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) > len(nums2):
            nums2,nums1 = nums1,nums2
            
        l,h = 0,len(nums1)-1
        half = (len(nums1)+len(nums2))// 2
            
        while True:
            cut1 = l+(h-l)//2
            cut2 = half-(cut1+1)-1
            
            l1 = nums1[cut1] if cut1>=0 else float("-inf")
            l2 = nums2[cut2] if cut2>=0 else float("-inf")
            r1 = nums1[cut1+1] if cut1+1<len(nums1) else float("inf")
            r2 = nums2[cut2+1] if cut2+1<len(nums2) else float("inf")
            
            if l1<=r2 and l2<=r1:
                if (len(nums1)+len(nums2))%2 != 0:
                    return min(r1,r2)
                else:
                    return (max(l1,l2)+min(r1,r2))/2
            elif l1>r2:
                h = cut1-1
            else:
                l = cut1+1
        
