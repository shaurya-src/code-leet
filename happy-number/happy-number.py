class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        num = list(map(int, str(n)))
        oc = set()
        oc.add(n)
        while len(num) > 0:
            sq = sum([x**2 for x in num])
            if sq in oc:
                return False
            else:
                oc.add(sq)
            num = list(map(int, str(sq)))
            if sq == 1:
                return True
            
        return False
            