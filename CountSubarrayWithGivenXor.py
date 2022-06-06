class Solution:
	def numSubarrayWithXOR(self, A: List[int], target: int) -> int:
		xor = 0
		freq = {}
		c = 0
		n = len(A)
		
		for i in range(n):
			xor = xor^A[i]
			
			if (xor^target) in freq:
				c+= freq[xor^target]
			if xor == target:
				c+=1
			if xor in freq:
				freq[xor]+=1
			else:
				freq[xor] = 1
		
		return c
				
		


