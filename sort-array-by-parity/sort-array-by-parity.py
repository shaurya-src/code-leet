class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd = []
        even = []
        for num in A:
            if num%2 == 0:
                even.append(num)
            else:
                odd.append(num)
        return even + odd