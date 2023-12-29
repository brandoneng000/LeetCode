from typing import List

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        
        cache = {}

        def helper(i: int, d: int, cur_max: int):
            if i == len(jobDifficulty):
                return 0 if d == 0 else float('inf')
            if d == 0:
                return float('inf')
            
            if (i, d, cur_max) in cache:
                return cache[(i, d, cur_max)]

            cur_max = max(cur_max, jobDifficulty[i])
            res = min(helper(i + 1, d, cur_max), cur_max + helper(i + 1, d - 1, -1))
            cache[(i, d, cur_max)] = res

            return res

        return helper(0, d, -1)
        
        
def main():
    sol = Solution()
    print(sol.minDifficulty(jobDifficulty = [6,5,4,3,2,1], d = 2))
    print(sol.minDifficulty(jobDifficulty = [9,9,9], d = 4))
    print(sol.minDifficulty(jobDifficulty = [1,1,1], d = 3))

if __name__ == '__main__':
    main()