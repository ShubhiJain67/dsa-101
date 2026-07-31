class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.findFirst(nums, target), self.findLast(nums, target)]

    def findFirst(self, nums, target):
        low = 0
        high = len(nums) - 1
        ans = -1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                ans = mid
                high = mid - 1      # Continue searching left
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def findLast(self, nums, target):
        low = 0
        high = len(nums) - 1
        ans = -1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                ans = mid
                low = mid + 1       # Continue searching right
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return ans
