class Solution:
	def detectCycle(self, V, adj):
		edges = []
		parents = [i for i in range(V)]
		ranks = [0] * V
		
		for node in range(V):
		    for neigh in adj[node]:
		        if node < neigh and (not self.union(node, neigh, parents, ranks)):
		            return True
		return False
	
    def union(self, element1, element2, parents, ranks):
        parent1 = self.find(element1, parents)
        parent2 = self.find(element2, parents)
        if parent1 == parent2:
            return False
        rank1 = ranks[parent1]
        rank2 = ranks[parent2]
        if rank1 == rank2:
            parents[parent1] = parent2
            parent2 += 1
        elif rank1 > rank2:
            parents[parent2] = parent1
        else:
            parents[parent1] = parent2
        return True
	
	def find(self, element, parents):
	    if element == parents[element]:
	        return element
	    parents[element] = self.find(parents[element], parents)
	    return parents[element]
		
