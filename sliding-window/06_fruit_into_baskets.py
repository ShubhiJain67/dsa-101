from typing import List
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {}
        p0 = 0
        p1 = 0
        maxCount = 0
        while p1 < len(fruits):
            if len(basket) == 2 and fruits[p1] not in basket:
                currFruits = basket.keys()
                farthest = len(fruits)
                fruitToRemove = None
                for fruit in currFruits:
                    if farthest > basket[fruit]:
                        fruitToRemove = fruit
                        farthest = basket[fruit]
                p0 = basket[fruitToRemove] + 1
                del basket[fruitToRemove]
            
            basket[fruits[p1]] = p1
            maxCount = max(p1-p0+1,maxCount)
            p1 += 1
        
        return maxCount
