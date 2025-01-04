from collections import Counter
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        left_side = set()
        right_side = Counter(s)

        for mid in s:
            right_side[mid]-=1
            for char in left_side:
                if right_side[char]>0:
                    res.add((mid, char))
            left_side.add(mid)
        
        return len(res)

sol = Solution()
print(sol.countPalindromicSubsequence(s = "aabca"))