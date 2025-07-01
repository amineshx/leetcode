class Solution:
    def maxDifference(self, s: str) -> int:
        hashmap = {}
        for char in s:
            if char in hashmap:
                hashmap[char]+=1 
            else :
                hashmap[char]=1
        odds = []
        evens = []
        for val in hashmap.values():
            if val%2==0:
                evens.append(val)
            else:
                odds.append(val)
        res = - float('inf')
        for o in odds:
            for e in evens:
                res = max(res,o-e)
        return res

sol = Solution()
print(sol.maxDifference(s = "aaaaabbc"))
