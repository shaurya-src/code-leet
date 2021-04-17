class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length = min(len(word1), len(word2))
        result = ''
        for i in range(length):
            result += word1[i] + word2[i]
        try:
            result += word1[length:]
            result += word2[length:]
        except Exception:
            pass
        return result