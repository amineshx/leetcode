class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split()
        for i,char in enumerate(sentence):
            if char.startswith(searchWord):
                return i+1
        return -1
