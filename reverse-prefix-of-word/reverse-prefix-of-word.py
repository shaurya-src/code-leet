class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        try:
            idx = word.index(ch) + 1
        except Exception:
            return word
        return ''.join(word[:idx][::-1] + word[idx:])