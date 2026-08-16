''' Structure of binary tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque
import math

class Solution:
    def minTime(self, root, target):
        # code here
        return self.viaAdjList(root, target)
        
    def viaAdjList(self, root, target): # O(n) O(n)
        adj = self.getAdjList(root)
        que = deque([[target, 0]])
        visited = set()
        minTime = -math.inf
        while que:
            curr, time = que.popleft()
            if curr in visited:
                continue
            if time > minTime:
                minTime = time
            visited.add(curr)
            if curr in adj:
                for neigh in adj[curr]:
                    if neigh not in visited:
                        que.append([neigh, time + 1])
        return minTime
    
    def getAdjList(self, root):
        adjList = {}
        que = deque([root])
        while que:
            curr = que.popleft()
            if curr.data not in adjList:
                adjList[curr.data] = []
            if curr.left:
                if curr.left.data not in adjList:
                    adjList[curr.left.data] = []
                adjList[curr.left.data].append(curr.data)
                adjList[curr.data].append(curr.left.data)
                que.append(curr.left)
            if curr.right:
                if curr.right.data not in adjList:
                    adjList[curr.right.data] = []
                adjList[curr.right.data].append(curr.data)
                adjList[curr.data].append(curr.right.data)
                que.append(curr.right)
        return adjList
        
        
