class Solution(object):
    def isValid(self, s):
        brackets_map = {')': '(', ']': '[', '}': '{'}
        stack = []

        for c in s:
            if c in brackets_map:
                if not stack or stack[-1] != brackets_map[c]:
                    return False

                stack.pop()
            else:
                stack.append(c)

        return not stack
