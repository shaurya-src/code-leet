class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if len(strs) == 1:
            return strs[0]
        
        words = sorted(strs)
        
        if  len(strs)<1 or len(words[0])<1 or words[0][0] != words [-1][0]:
            return ""
        

        
        result = ""
        
        n = min(len(words[0]), len(words[-1]))
        
        for i in range(n):
            if words[0][i] != words[-1][i]:
                break
            else:
                result += words[0][i]
        return result
        
    
        