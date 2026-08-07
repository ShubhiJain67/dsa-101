from typing import List
class Solution:
    def combinationSum4(self, candidates: List[int], Target: int) -> int:
        # combinations = self.getCombRec(candidates, Target, 0)

        # memory = [[None]*(len(candidates)+1) for _ in range(Target+1)]
        # combinations = self.getCombRecMemo(candidates, Target, 0, memory)

        # combinations = self.getCombDP(candidates, Target)
        # unique = {}
        # count = 0
        # for comb in combinations:
        #     combStr = str(comb)
        #     if combStr not in unique:
        #         unique[combStr] = True
        #         count+=1

        count = self.getCombDPV2(candidates, Target)

        return count

    def getCombRec(self, candidates, target, index):
        combinations = []
        if target == 0:
            combinations = [[]]
        elif index == len(candidates):
            combinations = []
        else:
            withoutAndContinueCombinations = self.getCombRec(candidates, target, index+1)
            combinations = withoutAndContinueCombinations
            if target - candidates[index] >= 0:
                withAndStayCombinations = self.getCombRec(candidates, target - candidates[index], index)
                for comb in withAndStayCombinations:
                    if len(comb) == 0:
                        combinations.append([candidates[index]])
                    else:
                        for i in range(len(comb)+1):
                            combinations.append(comb[:i] + [candidates[index]] + comb[i:])
        return combinations

    def getCombRecMemo(self, candidates, target, index, memory):
        combinations = []
        if target == 0:
            combinations = [[]]
        elif index == len(candidates):
            combinations = []
        elif memory[target][index] != None:
            return memory[target][index]
        else:
            withoutAndContinueCombinations = self.getCombRecMemo(candidates, target, index+1, memory)
            combinations = withoutAndContinueCombinations
            if target - candidates[index] >= 0:
                withAndStayCombinations = self.getCombRecMemo(candidates, target - candidates[index], index, memory)
                for comb in withAndStayCombinations:
                    if len(comb) == 0:
                        combinations.append([candidates[index]])
                    else:
                        for i in range(len(comb)+1):
                            combinations.append(comb[:i] + [candidates[index]] + comb[i:])
        memory[target][index] = combinations
        return combinations

    def getCombDP(self, candidates, Target):
        memory = [[None]*(len(candidates)+1) for _ in range(Target+1)]

        for index in range(len(candidates), -1, -1):
            for target in range(Target+1):
                combinations = []
                if target == 0:
                    combinations = [[]]
                elif index == len(candidates):
                    combinations = []
                else:
                    withoutAndContinueCombinations = memory[target][index+1]
                    combinations = withoutAndContinueCombinations
                    if target - candidates[index] >= 0:
                        withAndStayCombinations = memory[target - candidates[index]][index]
                        for comb in withAndStayCombinations:
                            if len(comb) == 0:
                                combinations.append([candidates[index]])
                            else:
                                for i in range(len(comb)+1):
                                    combinations.append(comb[:i] + [candidates[index]] + comb[i:])
                memory[target][index] = combinations
        return memory[Target]

    
    def getCombDPV2(self, candidates, target):
        dp = [0] * (target + 1)
        dp[0] = 1

        for t in range(1, target + 1):
            for candidate in candidates:
                if t >= candidate:
                    dp[t] += dp[t - candidate]

        return dp[target]
