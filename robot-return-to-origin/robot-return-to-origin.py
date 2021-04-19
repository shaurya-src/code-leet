class Solution:
    def judgeCircle(self, moves: str) -> bool:
        h_pos = 0
        v_pos = 0
        
        for move in moves:
            if move == 'U':
                v_pos += 1
            elif move == 'D':
                v_pos -= 1
            elif move == 'L':
                h_pos -= 1
            elif move == 'R':
                h_pos += 1
                
        if h_pos == 0 and v_pos == 0:
            return True
        
        return False
            