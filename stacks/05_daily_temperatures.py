class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [[-1,0]]
        ans = []
        for index in range(len(temperatures)-1,-1,-1):
            # print(stack)
            temprature = temperatures[index]
            while stack[-1][0] != -1 and stack[-1][0] <= temprature:
                stack.pop()
            ans.append(stack[-1][1] if stack[-1][1] == 0 else stack[-1][1] - index)
            stack.append([temprature, index])
        ans.reverse()
        return ans
