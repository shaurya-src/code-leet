class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_w = 0
        for i in range(len(accounts)):
            cp = sum([x for x in accounts[i]])
            if cp > max_w:
                max_w = cp
        return max_w