from typing import List
class Solution:

    def kosaraju(self, V, edges):
        adjList = self.getAdjList(V, edges)
        topoSort = self.getTopoSort(V, adjList)
        # print(topoSort)
        reversedEdges = self.reverseEdges(edges)
        reversedAdjList = self.getAdjList(V, reversedEdges)
        componentCount = self.getStronglyConnectedComponnets(topoSort, V, reversedAdjList)
        return componentCount
            
    def getAdjList(self, V, edges):
        adjList = [[] for _ in range(V)]
        for src, dest in edges:
            adjList[src].append(dest)
        return adjList
    
    def getTopoSort(self, V, adjList):
        visitedNodes = [False]*V
        topoSort = []
        for node in range(V):
            if not visitedNodes[node]:
                self.topoSort(adjList, node, topoSort, visitedNodes)
        topoSort.reverse()
        return topoSort
    
    def topoSort(self, adjList, node, topoSort, visitedNodes):
        if visitedNodes[node]:
            return
        visitedNodes[node] = True
        for neigh in adjList[node]:
            if visitedNodes[neigh]:
                continue
            self.topoSort(adjList, neigh, topoSort, visitedNodes)
        topoSort.append(node)

    def reverseEdges(self, edges):
        reversedEdges = []
        for edge in edges:
            reversedEdges.append([edge[1], edge[0]])
        return reversedEdges
        
    def getStronglyConnectedComponnets(self, topoSort, V, adjList):
        componentCount = 0
        visitedNodes = [False]*V
        for node in topoSort:
            if not visitedNodes[node]:
                self.dfs(adjList, node, visitedNodes)
                componentCount += 1
                # print(visitedNodes)
        return componentCount
        
    def dfs(self, adjList, node, visitedNodes):
        if visitedNodes[node]:
            return
        visitedNodes[node] = True
        for neigh in adjList[node]:
            self.dfs(adjList, neigh, visitedNodes)
        
        
        
