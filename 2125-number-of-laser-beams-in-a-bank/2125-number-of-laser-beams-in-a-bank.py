class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total_beams = 0
        curr_row, last_row = 0, 0
        
        for row in bank:
            curr_row = len([1 for ch in row if ch == '1'])
            total_beams += last_row * curr_row
            if curr_row > 0:
                last_row = curr_row
        return total_beams
                