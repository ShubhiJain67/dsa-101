class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        stack = []
        visited = set()

        for ch in s:
            freq[ord(ch) - ord('a')] -= 1
            if ch in visited:
                continue

            while (stack and stack[-1] > ch and freq[ord(stack[-1]) - ord('a')] > 0):
                topCh = stack.pop()
                visited.remove(topCh)

            stack.append(ch)
            visited.add(ch)

        return "".join(stack)
