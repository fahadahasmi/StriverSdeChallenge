class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, A):
        l = []
        
        for i in range(len(A)):
            for j in range(len(A[i])):
                l.append(A[i][j])
        
        l.sort()
        return l[len(l)//2]
