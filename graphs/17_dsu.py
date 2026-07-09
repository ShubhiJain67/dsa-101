class Solution:
    def DSU(self, n, queries):
        result = []
        parents = [i for i in range(n+1)]
        for query in queries:
            if query[0] == 1:
                self.performUnion(query[1], query[2], parents)
            elif query[0] == 2:
                parent = self.findParent(query[1], parents)
                result.append(parent)
        return result
    
    def performUnion(self, element1, element2, parents):
        parent1 = self.findParent(element1, parents)
        parent2 = self.findParent(element2, parents)
        if parent1 != parent2:
            parents[parent1] = parent2
    
    def findParent(self, element, parents):
        if element == parents[element]:
            return element
        return self.findParent(parents[element], parents)
        
