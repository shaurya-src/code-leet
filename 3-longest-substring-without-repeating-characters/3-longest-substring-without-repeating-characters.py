class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        global_max = 0
        buffer = []
        for ch in s:
            if ch in buffer:
                idx = buffer.index(ch)
                buffer = buffer[idx+1:]
            
            buffer.append(ch)
            global_max = max(global_max, len(buffer))
        
        return global_max