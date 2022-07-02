from math import comb
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(combo: List[int], pos, target):
            if target == 0:
                res.append(combo.copy())
                return
            if target <= 0:
                return
            
            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                combo.append(candidates[i])
                backtrack(combo, i + 1, target - candidates[i])
                combo.pop()
                prev = candidates[i]

        backtrack([], 0, target)
        return res

def main():
    sol = Solution()
    print(sol.combinationSum2([10,1,2,7,6,1,5], 8))
    print(sol.combinationSum2([2,5,2,1,2], 5))

if __name__ == '__main__':
    main()