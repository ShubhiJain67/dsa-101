class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        store = {}
        for task in tasks:
            if task not in store:
                store[task] = 0
            store[task] += 1
        available = []
        for task in store:
            available.append([-store[task], task])
        heapq.heapify(available)
        atRest = {}
        time = 0
        while available or atRest:
            time += 1
            currNode = None
            if available:
                count , currNode = heapq.heappop(available)
                count = count * -1
                if count > 1:
                    atRest[currNode] = [n+1, count - 1]
            newAtRest = {}
            for node in atRest:
                atRest[node][0] -= 1
                if atRest[node][0] == 0:
                    heapq.heappush(available, [-atRest[node][1], node])
                else:
                    newAtRest[node] = atRest[node]
            atRest = newAtRest
                    
        return time
            

