class Solution:
    def DSU(self, n, queries):
        result = []
        sizes = [1]*(n+1)
        parents = [i for i in range(n+1)]
        for query in queries:
            if query[0] == 1:
                self.performUnionWithSize(query[1], query[2], parents, sizes)
            elif query[0] == 2:
                parent = self.findParentWithPathCompression(query[1], parents)
                result.append(parent)
        return result
    
    def performUnionWithSize(self, element1, element2, parents, sizes):
        parent1 = self.findParentWithPathCompression(element1, parents)
        parent2 = self.findParentWithPathCompression(element2, parents)
        if parent1 == parent2:
            return
        size1 = sizes[parent1]
        size2 = sizes[parent2]
        if size1 >= size2:
            parents[parent2] = parent1
            sizes[parent2] += sizes[parent1]
        else:
            parents[parent1] = parent2
            sizes[parent1] += sizes[parent2]
        
    def findParentWithPathCompression(self, element, parents):
        if element == parents[element]:
            return element
        parents[element] = self.findParentWithPathCompression(parents[element], parents)
        return parents[element]
