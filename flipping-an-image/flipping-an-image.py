class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        result = image.copy()
        for i,row in enumerate(image):
            result[i] = row[::-1]
            result[i] = [0 if x == 1 else 1 for x in result[i]]
        
        return result