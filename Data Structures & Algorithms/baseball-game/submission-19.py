class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = 0
        stack = []
        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                stack.append(2 * stack[-1])
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
        for m in range(len(stack)):
            res += stack[m]
        return res      