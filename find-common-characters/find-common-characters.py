class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        pos = [self.dct(word) for word in words]
        alpha = pos[0]
        res = []
        print(pos)
        for key, value in alpha.items():
            flag = True
            oc = value
            for i in range(1, len(pos)):
                if key not in pos[i]:
                    flag = False
                    break
                else:
                    oc = min(oc, pos[i][key])
            
            if flag:
                res.extend([key]*oc)
        return res
    
    def dct(self, word):
        c = {}
        for ch in word:
            if ch in c:
                c[ch] += 1
            else:
                c[ch] = 1
        return c