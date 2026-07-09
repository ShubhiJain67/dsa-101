class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        connectComponents = self.getConnectedComponentsDSU(n, edges)
        count = 0
        # TIME CONSUMING
        # for i in range(len(connectComponents)):
        #     for j in range(i+1, len(connectComponents)):
        #         count += len(connectComponents[i])*len(connectComponents[j])
        remaining = n
        for component in connectComponents:
            size = len(component)
            remaining -= size
            count += size * remaining
        return count

    def getAdjList(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = [[] for _ in range(n)]
        for node1, node2 in edges:
            adj[node1].apepnd(node2)
            adj[node2].apepnd(node1)
        return adj
    
    def getConnectedComponentsDSU(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        parents = [i for i in range(n)]
        ranks = [0] * n
        for source, dest in edges:
            self.union(source, dest, parents, ranks)
        
        components = [[] for i in range(n)]
        for i in range(n):
            parent = self.find(i, parents)
            components[parent].append(i)
        return [comp for comp in components if len(comp) > 0]
    
    def union(self, ele1, ele2, parents, ranks):
        parent1 = self.find(ele1, parents)
        parent2 = self.find(ele2, parents)
        if parent1 == parent2:
            return
        rank1 = ranks[parent1]
        rank2 = ranks[parent2]
        if rank1 == rank2:
            parents[parent2] = parent1
            ranks[parent1] += 1
        elif rank1 > rank2:
            parents[parent2] = parent1
        else:
            parents[parent1] = parent2
    
    def find(self, ele, parents):
        if ele == parents[ele]:
            return ele
        parents[ele] = self.find(parents[ele], parents)
        return parents[ele]
    
