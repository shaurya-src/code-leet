class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        words = set(sentence)
        if (len(words) != 26):
            return False
        else:
            return True            