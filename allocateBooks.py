class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def books(self, A, B):
        if B>len(A):
            return -1
        
        def isPossible(arr,barier,k,n):
            pages = 0
            stud = 1 
            for i in range(n):
                if arr[i] >  barier:
                    return False
                elif arr[i] + pages > barier:
                    pages = arr[i]
                    stud += 1
                else:
                    pages += arr[i]
            
            if stud>k:
                return False
            return True
        
        
        l,h,res = min(A),sum(A),-1
        while l<=h:
            mid = (l+h)//2
            if isPossible(A,mid,B,len(A)):
                res = mid
                h = mid-1
            else:
                l = mid+1
        return res
