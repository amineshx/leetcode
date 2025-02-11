class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        for char in s:
            stack.append(char)
            if len(stack)>= len(part) and "".join(stack[-len(part):])==part:
                for _ in range(len(part)):
                    stack.pop()
        return "".join(stack)

sol = Solution()
print(sol.removeOccurrences(s = "daabcbaabcbc", part = "abc"))
print(sol.removeOccurrences(s = "axxxxyyyyb", part = "xy"))


