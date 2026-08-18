class Solution:
    def jobSequencing(self, deadline, profit):
        # return self.viaSort(deadline, profit)
        return self.viaDSU(deadline, profit)
        
    def viaDSU(self, deadline, profit):
        jobs = []
        for i in range(len(deadline)):
            jobs.append((profit[i], deadline[i]))
        jobs.sort(reverse=True)
        maxDeadline = max(deadline)
        parent = [i for i in range(maxDeadline + 1)]

        totalProfit = 0
        jobCount = 0

        for currProfit, currDeadline in jobs:
            slot = self.find(parent, currDeadline)
            if slot > 0:
                totalProfit += currProfit
                jobCount += 1
                parent[slot] = self.find(parent, slot - 1)
        return [jobCount, totalProfit]

    def find(self, parent, x):
        if parent[x] == x:
            return x
        # Path compression
        parent[x] = self.find(parent, parent[x])
        return parent[x]
        
        
    def viaSort(self, deadline, profit):
        jobs = []
        for i in range(len(deadline)):
            jobs.append([profit[i], deadline[i]])
        jobs.sort(reverse = True)
        jobAlotment = [None]*(max(deadline)+1)
        for currProfit, currDeadLine in jobs:
            for t in range(currDeadLine, 0, -1):
                if jobAlotment[t] is None:
                    jobAlotment[t] = currProfit
                    break
            
        totalProfit = 0
        jobCount = 0
        for j in jobAlotment:
            if j is not None:
                jobCount += 1
                totalProfit += j
        return [jobCount,totalProfit]
        
