class Solution:
    def minOperations(self, n: int) -> int:
        exp = [(2*i)+1 for i in range(n)]
        target = sum(exp)//n
        count = 0
        for num in exp:
            if target == num:
                pass
            elif target > num:
                # off_pos.append(target-num)
                count += target-num
            else:
                # off_neg.append(num-target)
                pass
                
        # print(off_pos)
        # print(off_neg)
        return count