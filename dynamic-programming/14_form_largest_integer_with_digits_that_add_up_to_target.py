class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        # comb = self.getNumRec(cost, target, 1)

        # memory = [[[]]*(len(cost)+1) for _ in range(target+1)]
        # comb = self.getNumRecMemo(cost, target, 1, memory)

        # comb = self.getNumDp(cost, target)

        comb = self.getNumDpV2(cost, target)
        
        if comb == None:
            return "0"
        return comb

    def isStrGreater(self, str1, str2):
        if str1 == None:
            return True
        if str2 == None:
            return False
        if len(str1) < len(str2):
            return True
        if len(str1) == len(str2) and str1 < str2:
            return True
        return False

    def getNumRec(self, cost, target, index):
        comb = None
        if target == 0:
            comb = ""
        elif index == len(cost)+1:
            comb = None
        else:
            if target-cost[index-1] >= 0:
                withAndStay = self.getNumRec(cost, target-cost[index-1], index)
                if withAndStay is not None:
                    i = len(withAndStay)
                    for j in range(len(withAndStay)):
                        if withAndStay[j] < str(index):
                            i = j
                            break
                    withAndStay = withAndStay[:i]+str(index)+withAndStay[i:]
                    if self.isStrGreater(comb, withAndStay):
                        comb = withAndStay
            withoutAndContinue = self.getNumRec(cost, target, index+1)
            if self.isStrGreater(comb, withoutAndContinue):
                comb = withoutAndContinue
        return comb

    def getNumRecMemo(self, cost, target, index, memory):
        comb = None
        if target == 0:
            comb = ""
        elif index == len(cost)+1:
            comb = None
        elif memory[target][index-1] != []:
            return memory[target][index-1]
        else:
            if target-cost[index-1] >= 0:
                withAndStay = self.getNumRecMemo(cost, target-cost[index-1], index, memory)
                if withAndStay is not None:
                    i = len(withAndStay)
                    for j in range(len(withAndStay)):
                        if withAndStay[j] < str(index):
                            i = j
                            break
                    withAndStay = withAndStay[:i]+str(index)+withAndStay[i:]
                    if self.isStrGreater(comb, withAndStay):
                        comb = withAndStay
            withoutAndContinue = self.getNumRecMemo(cost, target, index+1, memory)
            if self.isStrGreater(comb, withoutAndContinue):
                comb = withoutAndContinue
        memory[target][index-1] = comb
        return memory[target][index-1]

    def getNumDp(self, cost, Target):
        memory = [[[]]*(len(cost)+1) for _ in range(Target+1)]
        for index in range(len(cost)+1, -1, -1):
            for target in range(Target+1):
                comb = None
                if target == 0:
                    comb = ""
                elif index == len(cost)+1:
                    comb = None
                else:
                    if target-cost[index-1] >= 0:
                        withAndStay = memory[target-cost[index-1]][index-1]
                        if withAndStay is not None:
                            i = len(withAndStay)
                            for j in range(len(withAndStay)):
                                if withAndStay[j] < str(index):
                                    i = j
                                    break
                            withAndStay = withAndStay[:i]+str(index)+withAndStay[i:]
                            if self.isStrGreater(comb, withAndStay):
                                comb = withAndStay
                    withoutAndContinue = memory[target][index]
                    if self.isStrGreater(comb, withoutAndContinue):
                        comb = withoutAndContinue
                memory[target][index-1] = comb
        return memory[Target][0]


    def getNumDpV2(self, cost, Target):
        prev = [[]]*(Target+1)
        for index in range(len(cost)+1, -1, -1):
            curr = [[]]*(Target+1)
            for target in range(Target+1):
                comb = None
                if target == 0:
                    comb = ""
                elif index == len(cost)+1:
                    comb = None
                else:
                    if target-cost[index-1] >= 0:
                        withAndStay = curr[target-cost[index-1]]
                        if withAndStay is not None:
                            i = len(withAndStay)
                            for j in range(len(withAndStay)):
                                if withAndStay[j] < str(index):
                                    i = j
                                    break
                            withAndStay = withAndStay[:i]+str(index)+withAndStay[i:]
                            if self.isStrGreater(comb, withAndStay):
                                comb = withAndStay
                    withoutAndContinue = prev[target]
                    if self.isStrGreater(comb, withoutAndContinue):
                        comb = withoutAndContinue
                curr[target] = comb
            prev = curr
        return prev[Target]

    
