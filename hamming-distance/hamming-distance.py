class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        def getBin(num):
            return "{:b}".format(num)
        
        bin1 = getBin(x)
        bin2 = getBin(y)
        c = 0
        if len(bin1) != len(bin2):
            if len(bin1) > len(bin2):
                pre = '0' * (len(bin1) - len(bin2))
                bin2 = pre + bin2
            else:
                pre = '0' * (len(bin2) - len(bin1))
                bin1 = pre + bin1
        if x==y:
            return 0
        else:
            for i in range(len(bin1)):
                if bin1[i] == bin2[i]:
                    pass
                else:
                    c += 1
            return c