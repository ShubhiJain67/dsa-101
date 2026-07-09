class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parents = {}
        for equation in equations:
            char1 = equation[0]
            operator = equation[1]
            char2 = equation[3]
            if char1 not in parents:
                parents[char1] = char1
            if char2 not in parents:
                parents[char2] = char2
            if operator == '=':
                self.union(char1, char2, parents)
        
        for equation in equations:
            char1 = equation[0]
            operator = equation[1]
            char2 = equation[3]
            if operator == '!':
                parent1 = self.find(char1, parents)
                parent2 = self.find(char2, parents)
                if parent1 != None and parent1 == parent2:
                    return False
        return True
        
    
    def union(self, element1: str, element2: str, parents):
        parent1 = self.find(element1, parents)
        parent2 = self.find(element2, parents)
        if parent1 == parent2:
            return
        parents[parent1] = parent2


    def find(self, element, parents):
        if element == parents[element]:
            return element
        return self.find(parents[element], parents)
        
