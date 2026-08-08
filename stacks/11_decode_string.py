class Solution:
    def decodeString(self, s: str) -> str:
        num = 0
        st = ""
        stack = []

        for ch in s:
            if ch.isdigit():
                if st:
                    stack.append(st)
                    st = ""
                num = num * 10 + int(ch)

            elif ch == '[':
                stack.append(num)
                num = 0

            elif ch.isalpha():
                st += ch

            else: 
                if st:
                    stack.append(st)
                    st = ""

                curr = ""
                while stack and isinstance(stack[-1], str):
                    curr = stack.pop() + curr

                repeat = stack.pop()

                stack.append(curr * repeat)

        if st:
            stack.append(st)

        return "".join(stack)
