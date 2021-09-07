class Solution:
    def sortString(self, s: str) -> str:
        dct = [0]*26
        for letter in s:
            dct[ord(letter)-ord('a')] += 1
        
        res = ""
        
        while len(res)!= len(s):
            # step 1-3
            for i,count in enumerate(dct):
                if count>0:
                    # print("one")
                    dct[i] -= 1
                    res += chr(i+ord('a'))

            # step 4-6
            for i in reversed(range(26)):
                if dct[i] > 0:
                    # print("two")
                    dct[i] -= 1
                    res += chr(i+ord('a'))
        return res