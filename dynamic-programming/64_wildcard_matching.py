class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # return self.match(s, p, 0, 0)

        # memo = [[None]*(len(p)+1) for _ in range(len(s)+1)]
        # return self.matchMemo(s, p, 0, 0, memo)

        # return self.matchDP(s, p)

        return self.matchDPV2(s, p)

    def match(self, s, p, si, pi):
        if si == len(s) and pi == len(p):
            return True
        if pi == len(p):
            return False
        if si == len(s):
            while pi < len(p):
                if p[pi] != '*':
                    return False
                pi += 1
            return True
        match = False
        if s[si] == p[pi]:
            match = self.match(s, p, si+1, pi+1)
        elif p[pi] == '?':
            match = self.match(s, p, si+1, pi+1)
        elif p[pi] == '*':
            match = self.match(s, p, si+1, pi+1) or self.match(s, p, si+1, pi) or self.match(s, p, si, pi+1)
        return match

    def matchMemo(self, s, p, si, pi, memo):
        if memo[si][pi] is not None:
            return memo[si][pi]
        match = False
        if si == len(s) and pi == len(p):
            match = True
        elif pi == len(p):
            match = False
        elif si == len(s):
            match = True
            while pi < len(p):
                if p[pi] != '*':
                    match = False
                    break
                pi += 1
        elif s[si] == p[pi]:
            match = self.matchMemo(s, p, si+1, pi+1, memo)
        elif p[pi] == '?':
            match = self.matchMemo(s, p, si+1, pi+1, memo)
        elif p[pi] == '*':
            match = self.matchMemo(s, p, si+1, pi+1, memo) or self.matchMemo(s, p, si+1, pi, memo) or self.matchMemo(s, p, si, pi+1, memo)
        memo[si][pi] = match
        return memo[si][pi]

    def matchDP(self, s, p):
        memo = [[None]*(len(p)+1) for _ in range(len(s)+1)]
        for si in range(len(s), -1, -1):
            for pi in range(len(p), -1, -1):
                match = False
                if si == len(s) and pi == len(p):
                    match = True
                elif pi == len(p):
                    match = False
                elif si == len(s):
                    match = True
                    tp = pi
                    while tp < len(p):
                        if p[tp] != '*':
                            match = False
                            break
                        tp += 1
                elif s[si] == p[pi]:
                    match = memo[si+1][pi+1]
                elif p[pi] == '?':
                    match = memo[si+1][pi+1]
                elif p[pi] == '*':
                    match = memo[si+1][pi+1] or memo[si+1][pi] or memo[si][pi+1]
                memo[si][pi] = match
        return memo[0][0]

    def matchDPV2(self, s, p):
        prev = [None]*(len(p)+1)
        for si in range(len(s), -1, -1):
            curr = [None]*(len(p)+1)
            for pi in range(len(p), -1, -1):
                match = False
                if si == len(s) and pi == len(p):
                    match = True
                elif pi == len(p):
                    match = False
                elif si == len(s):
                    match = True
                    tp = pi
                    while tp < len(p):
                        if p[tp] != '*':
                            match = False
                            break
                        tp += 1
                elif s[si] == p[pi]:
                    match = prev[pi+1]
                elif p[pi] == '?':
                    match = prev[pi+1]
                elif p[pi] == '*':
                    match = prev[pi+1] or prev[pi] or curr[pi+1]
                curr[pi] = match
            prev = curr
        return curr[0]
