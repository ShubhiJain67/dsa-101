class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = self.getAdjList(n, flights)
        
        # cheap = self.cheapestDFS(adjList, src, dst, k)

        # memo = [[[None] * (k + 1) for _ in range(n)] for _ in range(n)]
        # cheap = self.cheapestDFSMemo(adjList, src, dst, k, memo)

        cheap = self.cheapestBFS(n, adjList, src, dst, k)
        
        if cheap == math.inf:
            return -1
        return cheap

    def cheapestDFS(self, adjList, src, dst, k):
        if k == -1:
            return 0 if src == dst else math.inf
        cheap = math.inf
        if src == dst:
            cheap = 0
        else:
            for neigh, wt in adjList[src]:
                cheap = min(cheap, wt + self.cheapestDFS(adjList, neigh, dst, k-1))
        return cheap

    def cheapestDFSMemo(self, adjList, src, dst, k, memo):
        if k == -1:
            return 0 if src == dst else math.inf
        if memo[src][dst][k] is not None:
            return memo[src][dst][k]
        cheap = math.inf
        if src == dst:
            cheap = 0
        else:
            for neigh, wt in adjList[src]:
                cheap = min(cheap, wt + self.cheapestDFSMemo(adjList, neigh, dst, k-1, memo))
        memo[src][dst][k] = cheap
        return memo[src][dst][k]

    def getAdjList(self, n, flights):
        adjList = [[] for _ in range(n)]
        for (src, dst, wt) in flights:
            adjList[src].append([dst, wt])
        return adjList

    def cheapestBFS(self, n, adjList, src, dst, k):
        que = deque([[src, 0, -1]])
        minCost = [math.inf]*n
        while que:
            node, weight, stops = que.popleft()
            if minCost[node] > weight:
                 minCost[node] = weight
            if node == dst or stops == k:
                continue
            for neigh, neighWeight in adjList[node]:
                if minCost[neigh] < weight + neighWeight:
                    continue
                que.append([neigh, weight + neighWeight, stops + 1])
        return minCost[dst]
    
    
    def cheapestBellmanFord(self, n, flights, src, dst, k):
        prevCost = [math.inf] * n
        prevCost[src] = 0

        for _ in range(k + 1):
            currCost = prevCost.copy()

            for s, d, price in flights:
                if prevCost[s] != math.inf:
                    currCost[d] = min(
                        currCost[d],
                        prevCost[s] + price
                    )

            prevCost = currCost

        return -1 if prevCost[dst] == math.inf else prevCost[dst]
