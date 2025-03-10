from collections import defaultdict
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        
        def func(k):
            count_vowel = defaultdict(int)
            count_non_vowel = 0
            res = 0
            left=0
            for right in range(len(word)):
                if word[right] in "aieou":
                    count_vowel[word[right]]+=1
                else:
                    count_non_vowel+=1
                while len(count_vowel)==5 and count_non_vowel>=k:
                    res+=(len(word)-right)
                    if word[left] in "aieou":
                        count_vowel[word[left]]-=1
                    else : count_non_vowel-=1

                    if count_vowel[word[left]]==0:
                        count_vowel.pop(word[left])
                    left+=1
            return res
        return func(k)-func(k+1)
            
sol = Solution()
print(sol.countOfSubstrings(word = "aeioqq", k = 1))
print(sol.countOfSubstrings(word = "aeiou", k = 0))
print(sol.countOfSubstrings(word = "ieaouqqieaouqq", k = 1))