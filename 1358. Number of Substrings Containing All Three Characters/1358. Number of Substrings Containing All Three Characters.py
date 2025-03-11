class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        left = 0
        char_count = {'a': 0, 'b': 0, 'c': 0}
        for right in range(len(s)):
            char_count[s[right]] += 1
            while char_count['a'] > 0 and char_count['b'] > 0 and char_count['c'] > 0:
                res += len(s) - right
                char_count[s[left]] -= 1
                left += 1
        
        return res

sol = Solution()
print(sol.numberOfSubstrings(s = "abcabc"))
print(sol.numberOfSubstrings(s = "aaacb"))
print(sol.numberOfSubstrings(s = "abc"))