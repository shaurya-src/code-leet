class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:       
        if ruleKey == "type":
            return len([1 for x in items if x[0]==ruleValue])
        elif ruleKey == "color":
            return len([1 for x in items if x[1]==ruleValue])
        else:
            return len([1 for x in items if x[2]==ruleValue])
        