class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        op = cl = n
        res = []
        s = ""
        self.recur(op, cl, s, res)
        return res
    
    def recur(self, op, cl, s, res):
        if op == cl == 0:
            res.append(s)
        
        else:
            if op > 0:
                s1 = s
                s1 += "("
                self.recur(op-1, cl, s1, res)
            if cl>op:
                s2 = s
                s2 += ")"
                self.recur(op, cl-1, s2, res)