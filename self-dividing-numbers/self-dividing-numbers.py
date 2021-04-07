class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        op = []
        for i in range(left, right+1):
            num_list = list(map(int, str(i)))
            
            if 0 in num_list:
                pass
            elif len(num_list) == 1:
                op.append(i)
            elif all([True if i%x==0 else False for x in num_list]):
                op.append(i)
            
        return op