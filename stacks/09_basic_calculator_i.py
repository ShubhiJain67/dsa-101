import re
class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        if s[0] != '(':
            s = f"({s})"
        answer = 0
        lastStarting = []
        stack = []
        tokens = [x.strip() for x in re.split(r"([()])", s) if x]
        for i in range(len(tokens)):
            token = tokens[i]
            if token != ')':
                stack.append(token)
            else:
                exp = ""
                while stack[-1] != '(':
                    exp = f"{stack[-1]}{exp}"
                    stack.pop()
                result = self.evaluate(exp)
                stack.pop()
                stack.append(str(result))
        exp = ""
        while stack:
            exp = f"{stack[-1]}{exp}"
            stack.pop()
        return int(self.evaluate(exp))
    
    def evaluate(self, expr):
        expr = self.simplify(expr)
        total = 0
        num = 0
        sign = -1 if expr[0] == '-' else 1

        for ch in expr+"+":
            if ch.isdigit():
                num = num * 10 + int(ch)
            else:
                total += sign * num
                sign = -1 if ch == '-' else 1
                num = 0
        # print(f"Evaluated {expr} -> {total}")
        return total

    def simplify(self, expr):
        newexpr = ""
        i = 0
        while i < len(expr):
            if expr[i] in ['+','-'] and i + 1 < len(expr) and expr[i+1] in ['+','-']:
                if expr[i] == '+':
                    newOp = expr[i+1]
                else:
                    if expr[i+1] == '+':
                        newOp = '-'
                    else:
                        newOp = "+"
                newexpr += newOp
                i += 1
            else:
                newexpr += expr[i]
            i += 1
        # print(f"Simplified {expr} to {newexpr}")
        return newexpr
