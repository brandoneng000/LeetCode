from typing import List

class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)
        dp = [0] * (n + 1)
        res = left = 0

        for right, val in enumerate(prizePositions):
            while prizePositions[left] < prizePositions[right] - k:
                left += 1
            
            dp[right + 1] = max(dp[right], right - left + 1)
            res = max(res, right - left + 1 + dp[left])

        return res
        
def main():
    sol = Solution()
    print(sol.maximizeWin(prizePositions = [1,1,2,2,3,3,5], k = 2))
    print(sol.maximizeWin(prizePositions = [1,2,3,4], k = 0))

if __name__ == '__main__':
    main()