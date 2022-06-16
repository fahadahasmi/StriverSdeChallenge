class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        
        def check(arr,n,mid,dist):
            
            c,cowPlace = 1,arr[0]
            for i in range(1,n):
                if arr[i]-cowPlace>=dist:
                    c+=1
                    cowPlace = arr[i]
                
                if c==mid:
                    return True
                
            return False
        
        
        position.sort()
        l,h=1,position[-1]-position[0]
        
        while l<=h:
            mid = (l+h)//2
            
            if check(position,len(position),m,mid):
                l = mid+1
            else:
                h = mid-1
        
        return h
