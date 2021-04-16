class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        first = s[:len(s)//2].lower()
        last = s[len(s)//2:].lower()
        
        vowels = ['a', 'e', 'i', 'o', 'u']
        
        cf = len([letter for letter in first if letter in vowels])
        cl = len([letter for letter in last if letter in vowels])
        
        return cl == cf
        