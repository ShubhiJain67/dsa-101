class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # O(n^3) O(1)
        # return self.bruteForce(nums)

        # O(n^2) O(1)
        # return self.optimisedBruteForce(nums)

        # O(n) O(1)
        return self.prefixSuffix(nums)

    # Kadane Algorithm is not INTIUTIVE
    def kadane(self, nums):
        pass

    def prefixSuffix(self, nums):
        # If had all positive numbers -> multiple all
        # If even negatives and rest positives -> multiple all
        # odd negatives and positives -> try removing 1 negative and get max (max will be wither on left of excluded negative or right of excluded negative)
        # If there is a 0 everything becomes zero so break down
        # O(n) O(1)

        prefixMax = -math.inf
        suffixMax = -math.inf
        currPrefix = 1
        currSuffix = 1
        for index in range(len(nums)):
            currPrefix *= nums[index]
            currSuffix *= nums[len(nums)-index-1]
            prefixMax = max(prefixMax, currPrefix)
            suffixMax = max(suffixMax, currSuffix)
            if currPrefix == 0:
                currPrefix = 1
            if currSuffix == 0:
                currSuffix = 1
        return max(prefixMax, suffixMax)



    def optimisedBruteForce(self, nums):
        # Optimised Brute Force - chek all sub arrays utilising prefix product - O(n^2) O(1)
        maxProd = -math.inf
        for start in range(len(nums)):
            currProd = 1
            for end in range(start, len(nums)):
                currProd *= nums[end]
                maxProd = max(currProd, maxProd)
                if currProd == 0:
                    break
        return maxProd
    
    def bruteForce(self, nums):
        # Brute Force - Get all sbarrays, get all products of every subarray O(n^3) O(1)
        maxProd = -math.inf
        for start in range(len(nums)):
            for end in range(start+1, len(nums)+1):
                currProd = 1
                for index in range(start, end):
                    currProd *= nums[index]
                    maxProd = max(currProd, maxProd)
                    if currProd == 0:
                        break
        return maxProd
