from typing import List
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ruleKey = { "type": 0, "color": 1, "name": 2 }[ruleKey]
        res = 0

        for item in items:
            if item[ruleKey] == ruleValue:
                res += 1
        
        return res
        
def main():
    sol = Solution()
    print(sol.countMatches([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], "color", "silver"))
    print(sol.countMatches([["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], "type", "phone"))

if __name__ == '__main__':
    main()