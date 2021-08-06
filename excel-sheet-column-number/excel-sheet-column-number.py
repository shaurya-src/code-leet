class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        i = len(columnTitle) - 1
        result = 0
        for letter in columnTitle:
            result += (ord(letter) - ord('A') + 1) * (26**i)
            i -= 1
        return result