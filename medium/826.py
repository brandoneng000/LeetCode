from typing import List
import bisect

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        profit_diff = {}
        res = 0
        max_profit = 0
        for d, p in sorted(zip(difficulty, profit)):
            max_profit = max(max_profit, p)
            profit_diff[d] = max_profit

        difficulty = sorted(set(difficulty))
        for w in worker:
            diff = bisect.bisect(difficulty, w) - 1
            if w >= difficulty[diff]:
                res += profit_diff[difficulty[diff]]
        
        return res



def main():
    sol = Solution()
    print(sol.maxProfitAssignment(difficulty = [68,35,52,47,86], profit = [67,17,1,81,3], worker = [92,10,85,84,82]))
    print(sol.maxProfitAssignment(difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]))
    print(sol.maxProfitAssignment(difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]))

if __name__ == '__main__':
    main()