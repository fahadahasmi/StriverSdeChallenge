class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]*i for i in range(1,numRows+1)]
    
        if numRows>2:
            for i in range(2,numRows):
                for j in range(len(ans[i])):
                    if j==0 or j==len(ans[i])-1:
                        continue
                    ans[i][j] = ans[i-1][j] + ans[i-1][j-1]
        #print(ans)       
        return ans
