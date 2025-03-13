
# sliding window "neive algorithm " O(len(haystack)*len(needle))
class Solution:
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

# KMP o(len(haystack)+len(needle))
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        