class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # return self.getAllRec(candidates, target, 0)

        # memory= [[None]*(target+1) for _ in range(len(candidates)+1)]
        # return self.getAllRecMemo(candidates, target, 0, memory)

        return self.getAllDP(candidates, target)

    def getAllRec(self, candidates, target, index):
        combinations = []
        if target == 0:
            combinations = [[]]
        elif index == len(candidates):
            return combinations
        else:
            if target - candidates[index] >= 0:
                withAndStayCombinations = self.getAllRec(candidates, target - candidates[index], index)
                for c in withAndStayCombinations:
                    combinations.append(c + [candidates[index]])
            withoutAndContinueCombinations = self.getAllRec(candidates, target, index+1)
            for c in withoutAndContinueCombinations:
                combinations.append(c)
        return combinations
    
    def getAllRecMemo(self, candidates, target, index, memory):
        combinations = []
        if target == 0:
            combinations = [[]]
        elif index == len(candidates):
            combinations = []
        elif memory[index][target] != None:
            return memory[index][target]
        else:
            if target - candidates[index] >= 0:
                withAndStayCombinations = self.getAllRecMemo(candidates, target - candidates[index], index, memory)
                for c in withAndStayCombinations:
                    combinations.append(c + [candidates[index]])
            withoutAndContinueCombinations = self.getAllRecMemo(candidates, target, index+1, memory)
            for c in withoutAndContinueCombinations:
                combinations.append(c)
        memory[index][target] = combinations
        return combinations
    
    def getAllDP(self, candidates, Target):
        memory= [[None]*(Target+1) for _ in range(len(candidates)+1)]
        for target in range(Target+1):
            for index in range(len(candidates), -1, -1):
                combinations = []
                if target == 0:
                    combinations = [[]]
                elif index == len(candidates):
                    combinations = []
                else:
                    if target - candidates[index] >= 0:
                        withAndStayCombinations = memory[target - candidates[index]][index]
                        for c in withAndStayCombinations:
                            combinations.append(c + [candidates[index]])
                    withoutAndContinueCombinations = memory[target][index+1]
                    for c in withoutAndContinueCombinations:
                        combinations.append(c)
                memory[index][target] = combinations
        return memory[0][Target]
        
