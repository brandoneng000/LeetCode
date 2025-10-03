from typing import List
from collections import Counter

class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        players = [Counter() for _ in range(n)]
        res = set()

        for x, y in pick:
            players[x][y] += 1

            if players[x][y] > x:
                res.add(x)
        
        return len(res)

        
def main():
    sol = Solution()
    print(sol.winningPlayerCount(n = 4, pick = [[0,0],[1,0],[1,0],[2,1],[2,1],[2,0]]))
    print(sol.winningPlayerCount(n = 5, pick = [[1,1],[1,2],[1,3],[1,4]]))
    print(sol.winningPlayerCount(n = 5, pick = [[1,1],[2,4],[2,4],[2,4]]))

if __name__ == '__main__':
    main()