class Solution:
	def maxSumIS(self, arr):
		# return self.maxSumRec(arr, 0, -1)
		
		# memo = [[None]*len(arr) for _ in range(len(arr))]
		# return self.maxSumRecMemo(arr, 0, -1, memo)
		
		#return self.maxSumDP(arr)
		
		return self.maxSumDPV2(arr)
		
	def maxSumRec(self, arr, index, prev):
		if index == len(arr):
			return 0
		maxSum = self.maxSumRec(arr, index+1, prev)
		if prev == -1 or arr[prev] < arr[index]:
			maxSum = max(maxSum, arr[index] + self.maxSumRec(arr, index+1, index))
		return maxSum
	    
	def maxSumRecMemo(self, arr, index, prev, memo):
		if index == len(arr):
			return 0
		if memo[index][prev+1] is not None:
			return memo[index][prev+1]
		maxSum = self.maxSumRecMemo(arr, index+1, prev, memo)
		if prev == -1 or arr[prev] < arr[index]:
			maxSum = max(maxSum, arr[index] + self.maxSumRecMemo(arr, index+1, index, memo))
		memo[index][prev+1] = maxSum
		return maxSum
	    
	def maxSumDP(self, arr):
		memo = [[0] * (len(arr) + 1) for _ in range(len(arr) + 1)]
		for index in range(len(arr) - 1, -1, -1):
			for prev in range(index - 1, -2, -1):
				maxSum = memo[index + 1][prev + 1]
				if prev == -1 or arr[prev] < arr[index]:
					maxSum = max(maxSum, arr[index] + memo[index + 1][index + 1])
				memo[index][prev + 1] = maxSum
		return memo[0][0]
        
	def maxSumDPV2(self, arr):
		old = [0] * (len(arr) + 1)
		for index in range(len(arr) - 1, -1, -1):
			curr = [0] * (len(arr) + 1)
			for prev in range(index - 1, -2, -1):
				maxSum = old[prev + 1]
				if prev == -1 or arr[prev] < arr[index]:
					maxSum = max(maxSum, arr[index] + old[index + 1])
				curr[prev + 1] = maxSum
			old = curr
		return old[0]
        
        