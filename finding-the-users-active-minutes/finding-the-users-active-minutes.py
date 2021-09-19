class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        dct = {}
        for log in logs:
            uid, umin = log
            if uid not in dct:
                dct[uid] = set()
            dct[uid].add(umin)
        
        res = [0]*k
        
        for uid, mins in dct.items():
            res[len(mins)-1] += 1
        
        return res