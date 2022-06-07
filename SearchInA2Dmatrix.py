class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        for i in range(m):
            
            l = 0 
            h = len(matrix[i])-1
            
            while l<=h:
                
                mid = (l+h)//2
                
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] < target:
                    l = mid+1
                else:
                    h = mid-1
        
        return False
