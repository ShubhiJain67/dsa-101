from typing import List
class Solution:
    def makeConnected(self, computerCount: int, connections: List[List[int]]) -> int:
        connectionCount = len(connections)
        if computerCount > connectionCount + 1:
            return -1
        parents = [comp for comp in range(computerCount)]
        extraConnectionCount = 0
        for connection in connections:
            computer1 = connection[0]
            computer2 = connection[1]
            extraConnectionCount += self.union(computer1, computer2, parents)
        
        computerPools = {}
        for computer in range(computerCount):
            parent = self.find(computer, parents)
            computerPools[parent] = True
        
        if extraConnectionCount >= len(computerPools) - 1:
            return len(computerPools) - 1
        return -1
    
    def union(self, computer1: int, computer2: int, parents: List[int]):
        parent1 = self.find(computer1, parents)
        parent2 = self.find(computer2, parents)
        if parent1 == parent2:
            return 1
        parents[parent2] = parent1
        return 0
        
    def find(self, computer, parents):
        if computer == parents[computer]:
            return computer
        parents[computer] = self.find(parents[computer], parents)
        return parents[computer]
