class Solution:
    def numberOfMatches(self, n: int) -> int:
        teams_r = n
        matches = 0
        
        while teams_r != 1:
            extra = False
            if teams_r % 2 != 0:
                teams_r -= 1
                extra = True
            
            teams_r -= teams_r//2
            matches += teams_r
            
            if extra:
                teams_r += 1
        
        return matches