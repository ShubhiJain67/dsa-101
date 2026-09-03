class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # return self.matchRec(s, p, 0, 0)
        
        # memo = [[None]*(len(p)+1) for _ in range(len(s)+1)]
        # return self.matchRecMemo(s, p, 0, 0, memo)
        
        return self.matchDP(s, p)
        
        
    def matchRec(self, s, p, si, pi):
        if si == len(s) and pi == len(p):
            return True

        elif si == len(s):
            if pi + 1 < len(p) and p[pi + 1] == "*":
                return self.matchRec(s, p, si, pi + 2)
            else:
                return False
        elif pi == len(p):
            return False
        elif (p[pi] == s[si] or p[pi] == '.') and (pi + 1 < len(p) and p[pi+1] == "*"):
            return self.matchRec(s, p, si+1, pi) or self.matchRec(s, p, si, pi+2)
        elif pi + 1 < len(p) and p[pi+1] == "*":
            return self.matchRec(s, p, si, pi+2)
        elif p[pi] == s[si] or p[pi] == '.':
            return self.matchRec(s, p, si+1, pi+1)
        return False
    
    
    def matchRecMemo(self, s, p, si, pi, memo):
        if memo[si][pi] is not None:
            return False
        
        isMatching = False
        if si == len(s) and pi == len(p):
            isMatching = True
        elif si == len(s):
            if pi + 1 < len(p) and p[pi + 1] == "*":
                isMatching = self.matchRecMemo(s, p, si, pi + 2, memo)
            else:
                isMatching = False
        elif pi == len(p):
            isMatching = False
        elif (p[pi] == s[si] or p[pi] == '.') and (pi + 1 < len(p) and p[pi+1] == "*"):
            isMatching = self.matchRecMemo(s, p, si+1, pi, memo) or self.matchRecMemo(s, p, si, pi+2, memo)
        elif pi + 1 < len(p) and p[pi+1] == "*":
            isMatching = self.matchRecMemo(s, p, si, pi+2, memo)
        elif p[pi] == s[si] or p[pi] == '.':
            isMatching = self.matchRecMemo(s, p, si+1, pi+1, memo)
        memo[si][pi] = isMatching
        return memo[si][pi]
    
    
    def matchDP(self, s, p):
        memo = [[None]*(len(p)+1) for _ in range(len(s)+1)]
        for si in range(len(s), -1, -1):
            for pi in range(len(p), -1, -1):
                isMatching = False
                if si == len(s) and pi == len(p):
                    isMatching = True
                elif si == len(s):
                    if pi + 1 < len(p) and p[pi + 1] == "*":
                        isMatching = memo[si][pi + 2]
                    else:
                        isMatching = False
                elif pi == len(p):
                    isMatching = False
                elif (p[pi] == s[si] or p[pi] == '.') and (pi + 1 < len(p) and p[pi+1] == "*"):
                    isMatching = memo[si+1][pi] or memo[si][pi + 2]
                elif pi + 1 < len(p) and p[pi+1] == "*":
                    isMatching = memo[si][pi + 2]
                elif p[pi] == s[si] or p[pi] == '.':
                    isMatching = memo[si+1][pi+1]
                memo[si][pi] = isMatching
        return memo[0][0]
    
