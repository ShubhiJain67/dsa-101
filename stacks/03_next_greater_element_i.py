class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = [-1]
        store = {}

        for i in range(len(nums2)-1,-1,-1):
            # print(stack)
            num = nums2[i]
            while stack[-1] < num and stack[-1] != -1:
                stack.pop()
            store[num] = stack[-1]
            stack.append(num)
                

        ans = []
        for num in nums1:
            ans.append(store[num])
        return ans
