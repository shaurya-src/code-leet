class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.strip().split()
        x = set(brokenLetters)
        count = 0
        for word in words:
            good = True
            for ch in word:
                if ch in x:
                    good = False
                    break
            if good:
                count += 1
            
        return count
        