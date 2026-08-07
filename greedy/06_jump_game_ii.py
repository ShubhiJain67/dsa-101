from typing import List
from collections import deque
class Solution:
    def jump(self, nums: List[int]) -> int:
        # return self.jumpRec(nums, 0)

        # memo = [None]*len(nums)
        # return self.jumpMemo(nums, 0, memo)

        # return self.jumpDP(nums)

        # return self.jumpGraph(nums)

        return self.jumpGreedy(nums)
    
    def jumpGreedy(self, nums):
        if len(nums) == 1:
            return 0
        goal = len(nums) - 1
        visited = [False]*len(nums)
        visited[0] = True
        que = deque([(0, 0)])
        while que:
            node, level = que.popleft()
            for adj in range(node+1, min(len(nums), node+nums[node]+1)):
                if not visited[adj]:
                    visited[adj] = True
                    if adj == goal:
                        return level+1
                    que.append((adj, level+1))
        return -1

    def jumpGraph(self, nums):
        if len(nums) == 1:
            return 0
        adjList = [[] for _ in range(len(nums))]
        for start in range(len(nums)):
            for end in range(start+1, start+nums[start]+1):
                if end < len(nums):
                    adjList[start].append(end)
        goal = len(nums) - 1
        visited = [False]*len(nums)
        visited[0] = True
        que = deque([(0, 0)])
        while que:
            node, level = que.popleft()
            for adj in adjList[node]:
                if not visited[adj]:
                    visited[adj] = True
                    if adj == goal:
                        return level+1
                    que.append((adj, level+1))
        return -1
    
    def jumpRec(self, nums, index):
        if index == len(nums)-1:
            return 0
        if index >= len(nums):
            return None
        minPath = float('inf')
        for i in range(1, nums[index]+1):
            dist = self.jumpRec(nums, index + i)
            if dist is not None:
                minPath = min(minPath, 1+dist)
        return minPath

    def jumpMemo(self, nums, index, memo):
        if index == len(nums)-1:
            return 0
        if index >= len(nums):
            return None
        if memo[index] is not None:
            return memo[index]
        minPath = float('inf')
        for i in range(1, nums[index]+1):
            dist = self.jumpMemo(nums, index + i, memo)
            if dist is not None:
                minPath = min(minPath, 1+dist)
        memo[index] = minPath
        return memo[index]

    def jumpDP(self, nums):
        memo = [None]*len(nums)
        for index in range(len(nums)-1, -1, -1):
            minPath = float('inf')
            if index == len(nums)-1:
                minPath = 0
            else:
                for i in range(1, nums[index]+1):
                    if index + i < len(nums) and memo[index + i] is not None:
                        minPath = min(minPath, 1+memo[index + i])
            memo[index] = minPath
        return memo[0]
