class Solution:
    def isValid(self, s: str) -> bool:
        chr1 = ['{','(','[']
        chr2 = ['}',')',']']
        stack = []
        for i in s:
            if i == '{' or i == '[' or i == '(':
                stack.append(i)
            elif not stack: return False
            elif i == chr2[0] and stack[len(stack)-1] == chr1[0]:
                stack.pop()
            elif i == chr2[1] and stack[len(stack)-1] == chr1[1]:
                stack.pop()
            elif i == chr2[2] and stack[len(stack)-1] == chr1[2]:
                stack.pop()
            else: return False
        if not stack:
            return True