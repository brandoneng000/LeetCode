from typing import List

class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        dp = [1, 0, 1]

        for obs in obstacles:
            if obs:
                dp[obs - 1] = float('inf')
            for i in range(3):
                if obs != i + 1:
                    dp[i] = min(dp[i], dp[(i + 1) % 3] + 1, dp[(i + 2) % 3] + 1)
        
        return min(dp)
        
def main():
    sol = Solution()
    print(sol.minSideJumps([0,1,2,3,0]))
    print(sol.minSideJumps([0,1,1,3,3,0]))
    print(sol.minSideJumps([0,2,1,0,3,0]))

if __name__ == '__main__':
    main()