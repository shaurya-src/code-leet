class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            test = set(word)
            if all(letter in allowed for letter in test):
                count += 1
        
        return count