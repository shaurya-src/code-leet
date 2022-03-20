class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        start = []
        mid = []
        end = []
        
        for num in nums:
            if num>pivot:
                end.append(num)
            elif num<pivot:
                start.append(num)
            else:
                mid.append(num)
                
        return start+ mid + end