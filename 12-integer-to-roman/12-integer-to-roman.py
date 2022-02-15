class Solution:
    def intToRoman(self, num: int) -> str:
        def getRoman(digit, start, beforeMid, mid, last):
            romanDigit = ''
            
            if digit == 0:
                return ''
            elif 1 <= digit <= 3:
                romanDigit += start*digit
            elif digit == 4:
                romanDigit += beforeMid
            elif 5 <= digit <= 8:
                romanDigit += mid + start*(digit-5)
            elif digit == 9:
                romanDigit += last
            
            return romanDigit
            
        numList = [int(x) for x in str(num)]
        idx = 0
        roman = ''
        for digit in reversed(numList):
            # ones place
            if idx == 0:
                roman += getRoman(digit, 'I', 'IV', 'V', 'IX')
            
            # tens place
            elif idx == 1:
                roman = getRoman(digit, 'X', 'XL', 'L', 'XC') + roman
            
            # hundreds place
            elif idx == 2:
                roman = getRoman(digit, 'C', 'CD', 'D', 'CM') + roman
            
            # thousands place
            elif idx == 3:
                roman = getRoman(digit, 'M', '', '', '') + roman
            
            idx += 1
            
        return roman