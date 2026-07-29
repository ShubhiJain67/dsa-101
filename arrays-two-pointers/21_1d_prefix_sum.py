class Solution:
    def prefSum(self, arr):
        # code here
        for i in range(1, len(arr)):
            arr[i] = arr[i]+arr[i-1]
        return arr
