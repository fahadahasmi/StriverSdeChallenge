#User function Template for python3
class Solution:
	def subsetSums(self, arr, N):
		# code here
		
		def helper(a,i,sum,ans):
		    if i==len(a):
		        ans.append(sum)
		        return
		    
		    helper(a,i+1,sum+a[i],ans)
		    helper(a,i+1,sum,ans)
		    
	    ans = []
	    helper(arr,0,0,ans)
	    return ans
