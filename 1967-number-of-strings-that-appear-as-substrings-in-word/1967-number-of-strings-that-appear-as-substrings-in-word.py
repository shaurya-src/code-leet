class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return len(['' for sub in patterns if sub in word])