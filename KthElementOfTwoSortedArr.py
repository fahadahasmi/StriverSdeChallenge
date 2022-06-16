class Solution:
    def kthElement(self,  nums1, nums2, n, m, k):
        
        def helper(arr1, arr2, m, n, k):
            if m > n:
                return helper(arr2, arr1, n, m, k)
            low = max(0, k - m)
            high = min(k, n)
            while low <= high:
                cut1 = (low + high) >> 1
                cut2 = k - cut1
                l1 = cut1 == 0 and float("-inf") or arr1[cut1 - 1]
                l2 = cut2 == 0 and float("-inf") or arr2[cut2 - 1]
                r1 = cut1 == n and float("inf") or arr1[cut1]
                r2 = cut2 == m and float("inf") or arr2[cut2]
                if l1 <= r2 and l2 <= r1:
                    return max(l1, l2)
                elif l1 > r2:
                    high = cut1 - 1
                else:
                    low = cut1 + 1
            return 1
        
        ans = helper(nums1,nums2,m,n,k)
        return ans
        
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m, k = sz[0], sz[1], sz[2]
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement( a, b, n, m, k))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
