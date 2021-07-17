class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = [None]*len(s.split())
        for word in s.rstrip().split(' '):
            index = int(word[-1]) - 1
            res[index] = word[:-1]
        return ' '.join(res)