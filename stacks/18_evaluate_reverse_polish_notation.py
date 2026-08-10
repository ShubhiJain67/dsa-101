class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                num2 = stack.pop()
                num1 = stack.pop()
                result = self.evaluate(num1, num2, token)
                stack.append(result)
            else:
                stack.append(token)
        return int(stack[-1])

    def evaluate(self, num1, num2, token):
        if token == "+":
            return f"{int(num1)+int(num2)}"
        if token == "-":
            return f"{int(num1)-int(num2)}"
        if token == "*":
            return f"{int(num1)*int(num2)}"
        if token == "/":
            return f"{int(int(num1)/int(num2))}"
