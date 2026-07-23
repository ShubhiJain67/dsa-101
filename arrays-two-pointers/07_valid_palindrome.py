class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) -1
        s = s.lower()
        while left < right:
            while right >= 0 and self.isNotAlphaNumeric(s[right]):
                right -=1
            while left < len(s) and self.isNotAlphaNumeric(s[left]):
                left +=1
            if left > right or right < 0 or left >= len(s):
                break
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    
    def isNotAlphaNumeric(self, ch):
        return not ((ch >= 'a' and ch <= 'z') or (ch >= '0' and ch <='9'))
