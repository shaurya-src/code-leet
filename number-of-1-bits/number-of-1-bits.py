class Solution:
    def hammingWeight(self, n: int) -> int:
        num = "{:b}".format(n)
        return len([1 for i in num if i != "0"])
    