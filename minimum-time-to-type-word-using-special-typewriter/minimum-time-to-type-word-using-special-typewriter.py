class Solution:
    def minTimeToType(self, word: str) -> int:
        # max cost for one round = 26//2 = 13
        # if cost is > 13; change direction
        min_cost = len(word)
        prev = 'a'
        for i, ch in enumerate(word):
            curr = abs(ord(prev) - ord(ch))
            print(curr)
            if curr > 13:
                min_cost += 26-curr
            else:
                min_cost += curr
            
            prev = ch
            
        return min_cost