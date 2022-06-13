class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def activitySelection(self,n,start,end):
        # code here
        arr = [i for i in range(n)]
        
        arr.sort(key = lambda x: [end[x],start[x],x])
        
        maxEnd = end[arr[0]]
        c = 1
        
        for i in range(1,len(arr)):
            if start[arr[i]] > maxEnd:
                c+=1 
                maxEnd = end[arr[i]]
        
        return c
