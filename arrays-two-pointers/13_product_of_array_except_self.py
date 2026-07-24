class Solution(object):
    def productExceptSelf(self, nums):
        # return self.bruteForce(nums)
        # return self.prefixProduct(nums)
        return self.prefixProductOptimised(nums)
    

    def prefixProductOptimised(self, nums):
        product = [1]*(len(nums))
        prefixProduct = 1
        i = 0
        while i < len(nums):
            product[i] = prefixProduct
            prefixProduct = prefixProduct * nums[i]
            i+=1
        
        suffixProduct = 1
        i = len(nums) - 1
        while i >= 0:
            product[i] *= suffixProduct
            suffixProduct = suffixProduct * nums[i]
            i-=1

        return product
    
    def prefixProduct(self, nums):
        prefixStore = [0]*(len(nums))
        prefixProduct = 1
        i = 0
        while i < len(nums):
            prefixStore[i] = prefixProduct
            prefixProduct = prefixProduct * nums[i]
            i+=1

        suffixStore = [0]*(len(nums))
        suffixProduct = 1
        i = len(nums) - 1
        while i >= 0:
            suffixStore[i] = suffixProduct
            suffixProduct = suffixProduct * nums[i]
            i-=1
        
        product = [0]*(len(nums))
        i = 0
        while i < len(nums):
            currProduct = 1
            currProduct =  currProduct * prefixStore[i]
            currProduct =  currProduct * suffixStore[i]
            product[i] = currProduct
            i+=1
        return product

    def bruteForce(self, nums):
        product = [1]*(len(nums))
        i = 0
        while i < len(nums):
            currProduct = 1
            j = 0
            while j < i - 1:
                currProduct *= nums[j]
                j += 1
            j = i+1
            while j < len(nums):
                currProduct *= nums[j]
                j += 1
            product[i] = currProduct
        return product
