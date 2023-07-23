from typing import List

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        res = 0
        score = 0
        seen = {}

        for i, h in enumerate(hours):
            score += 1 if h > 8 else -1
            if score > 0:
                res = i + 1
            seen.setdefault(score, i)
            if score - 1 in seen:
                res = max(res, i - seen[score - 1])
            
        return res
            

def main():
    sol = Solution()
    print(sol.longestWPI([9,9,6,0,6,6,9]))
    print(sol.longestWPI([6,6,6]))

if __name__ == '__main__':
    main()