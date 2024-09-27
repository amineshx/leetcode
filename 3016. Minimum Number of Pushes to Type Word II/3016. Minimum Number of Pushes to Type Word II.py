from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        sorted_counter = sorted(Counter(word).items(), key=lambda x: x[1], reverse=True)
        
        i = 1
        push = 0
        for _, count in sorted_counter:
            factor = (i - 1) // 8 + 1
            push += count * factor
            i += 1
        
        return push


res= Solution()
print(res.minimumPushes(word = "aabbccddeeffgghhiiiiii"))