class Solution:
    def knapsack(self, W, values, weights):
        # return self.knapsackProblemRecursion(W, values, weights, 0)
        
        # memory = [[None]*(W+1) for _ in range(len(values))]
        # return self.knapsackProblemMemoisation(W, values, weights, 0, memory)
        
        return self.knapsackProblemDP(W, values, weights)

    def knapsackProblemRecursion(self, W, values, weights, index):
        if index >= len(values) or W <= 0:
            return 0
        elif weights[index] > W:
            return self.knapsackProblemRecursion(W, values, weights, index+1)
        else:
            withoutItem = self.knapsackProblemRecursion(W, values, weights, index+1)
            withItem = values[index] + self.knapsackProblemRecursion(W-weights[index], values, weights, index+1)
            return withoutItem if withoutItem > withItem else withItem
    
    def knapsackProblemMemoisation(self, W, values, weights, index, memory):
        if index >= len(values) or W <= 0:
            return 0
        elif memory[index][W] != None:
            return memory[index][W]
        elif weights[index] > W:
            memory[index][W] = self.knapsackProblemMemoisation(W, values, weights, index+1, memory)
        else:
            withoutItem = self.knapsackProblemMemoisation(W, values, weights, index+1, memory)
            withItem = values[index] + self.knapsackProblemMemoisation(W-weights[index], values, weights, index+1, memory)
            memory[index][W] = withoutItem if withoutItem > withItem else withItem
        return memory[index][W]
        
    def knapsackProblemDP(self, W, values, weights):
        memory = [[None]*(W+1) for _ in range(len(values)+1)]
        for w in range(W+1):
            for index in range(len(values), -1, -1):
                if index == len(values) or w == 0:
                    memory[index][w] = 0
                elif weights[index] > w:
                    memory[index][w] = memory[index+1][w]
                else:
                    withoutItem = memory[index+1][w]
                    withItem = values[index] + memory[index+1][w-weights[index]]
                    memory[index][w] = withoutItem if withoutItem > withItem else withItem
        return memory[0][W]
                
