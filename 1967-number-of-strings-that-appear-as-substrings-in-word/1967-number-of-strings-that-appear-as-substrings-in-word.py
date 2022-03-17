class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        all_subs = set()
        for index in range(len(word)):
            for end in range(index+1, len(word)+1):
                all_subs.add(word[index:end])
        
        return len([1 for x in patterns if x in all_subs])