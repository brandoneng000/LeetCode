from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(index, combo: List[int], total):
            if total == target:
                res.append(combo.copy())
                return
            if total > target or index >= len(candidates):
                return
            
            combo.append(candidates[index])
            dfs(index, combo, total + candidates[index])
            combo.pop()
            dfs(index + 1, combo, total)

        dfs(0, [], 0)
        return res

def main():
    sol = Solution()
    print(sol.combinationSum([2,3,6,7], 7))
    print(sol.combinationSum([2,3,5], 8))

if __name__ == '__main__':
    main()