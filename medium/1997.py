from typing import List

class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        mod = 1000000007
        n = len(nextVisit)
        dp = [0] * n

        for i in range(1, n):
            dp[i] = (2 * dp[i - 1] - dp[nextVisit[i - 1]] + 2) % mod
        
        return dp[-1]
        
def main():
    sol = Solution()
    print(sol.firstDayBeenInAllRooms([0,0]))
    print(sol.firstDayBeenInAllRooms([0,0,2]))
    print(sol.firstDayBeenInAllRooms([0,1,2,0]))

if __name__ == '__main__':
    main()