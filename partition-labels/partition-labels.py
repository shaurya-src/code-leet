class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # store the last index of every character
        # take 2 pointers: left, right
        # left will keep track of senction start
        # increase left once a section is finalized
        # iterate S -> right = max(right, last_idx[s[i]])
        # this will make right keep track of upper limit
        # of possible section
        # once i == right, add section length to result
        
        last_idx = {char: idx for idx, char in enumerate(s)}
        result = []
        left, right = 0, 0
        for i, char in enumerate(s):
            right = max(right, last_idx[char])
            
            if i == right:
                result.append(right-left+1)
                left = i + 1
        return result