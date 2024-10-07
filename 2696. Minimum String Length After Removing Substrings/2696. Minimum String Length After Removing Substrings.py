class Solution:
    def minLength(self, s: str) -> int:
        i = 0
        while i<len(s)-1:
            if (s[i]=='A' and s[i+1]=='B') or (s[i]=='C' and s[i+1]=='D'):
                s = s[:i]+s[i+2:]
                i-=1
                print("s ",s)
                print("i ",i)
            else:
                i+=1
        return len(s)

# sol2 using a stack
class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for char in s:
            stack.append(char)
            if len(stack)>=2 and ((stack[-2]=='A' and stack[-1]=='B') or (stack[-2]=='C' and stack[-1]=='D')):
                stack.pop()
                stack.pop()
        return len(stack)
sol=Solution()
print(sol.minLength( s = "ABFCACDB"))