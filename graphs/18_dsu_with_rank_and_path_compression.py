class Solution:
    def DSU(self, n, queries):
        result = []
        ranks = [0]*(n+1)
        parents = [i for i in range(n+1)]
        for query in queries:
            if query[0] == 1:
                self.performUnionWithRank(query[1], query[2], parents, ranks)
            elif query[0] == 2:
                parent = self.findParentWithPathCompression(query[1], parents)
                result.append(parent)
        return result
    
    def performUnionWithRank(self, element1, element2, parents, ranks):
        parent1 = self.findParentWithPathCompression(element1, parents)
        parent2 = self.findParentWithPathCompression(element2, parents)
        if parent1 == parent2:
            return
        rank1 = ranks[parent1]
        rank2 = ranks[parent2]
        if rank1 == rank2:
            parents[parent1] = parent2
            ranks[parent2] += 1
        elif rank1 > rank2:
            parents[parent2] = parent1
        else:
            parents[parent1] = parent2
        
    def findParentWithPathCompression(self, element, parents):
        if element == parents[element]:
            return element
        parents[element] = self.findParentWithPathCompression(parents[element], parents)
        return parents[element]
