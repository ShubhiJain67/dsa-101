class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            addCurr = True
            while stack and stack[-1] > 0 and asteroid < 0:
                top = stack[-1]
                if top <= abs(asteroid):
                    stack.pop()
                if top >= abs(asteroid):
                    addCurr = False
                    break
            if addCurr:
                stack.append(asteroid)
        return stack
