#code java
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        sum = 0
        for i in ops:
            if i == "C": stack.pop()
            elif i == "D" and len(stack) > 0:
                n = len(stack)
                stack.append(stack[n-1] * 2)
            elif i == "+" and len(stack) > 0:
                n = len(stack)
                stack.append(stack[n - 1] + stack[n - 2])
            else: stack.append(int(i))
            print(stack)
        for i in stack: sum = sum + i
        return sums