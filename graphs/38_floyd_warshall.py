class Solution:
	def floydWarshall(self, dist):
		#Code here
		for midNode in range(len(dist)):
    		for sourceNode in range(len(dist)):
    		    for destNode in range(len(dist)):
    		        if dist[sourceNode][midNode] == 100000000 or dist[midNode][destNode] == 100000000:
    		            continue
    		        elif dist[sourceNode][midNode] + dist[midNode][destNode] < dist[sourceNode][destNode]:
    		            dist[sourceNode][destNode] = dist[sourceNode][midNode] + dist[midNode][destNode]
    	return dist
		
