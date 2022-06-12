import heapq
class Solution:
    
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        n = len(A)
        A.sort()
        B.sort()
        ans = [] 
        hs = set()
        temp = []
        i=n-1
        j=n-1
        hs.add((i,j))
        temp.append((-(A[i]+B[j]),(i,j)))
        for k in range(C):
            s ,(i,j) = heapq.heappop(temp)
            ans.append(-s)
            for iN,jN in [(i-1,j),(i,j-1)]:
                if iN>=0 and jN >=0 and (iN,jN) not in hs:
                    heapq.heappush(temp,(-(A[iN]+B[jN]),(iN,jN)))
                    hs.add((iN,jN))
        return ans 
