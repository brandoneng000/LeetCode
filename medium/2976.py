from typing import List
from collections import defaultdict

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        INF = 10000000 
        dist = [[INF for j in range(26)] for i in range(26)]
        res = 0

        for x, y, z in zip(original, changed, cost):
            start = ord(x) - ord('a')
            end = ord(y) - ord('a')
            dist[start][end] = min(dist[start][end], z)
        
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][k] == INF or dist[k][j] == INF:
                        continue

                    distance = dist[i][k] + dist[k][j]

                    if distance < dist[i][j]:
                        dist[i][j] = distance

        # for k in range(26):
        #     for i in range(26):
        #         for j in range(26):
        #             dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        for cur, goal in zip(source, target):
            if cur == goal:
                continue
            start = ord(cur) - ord('a')
            end = ord(goal) - ord('a')

            if dist[start][end] == INF:
                return -1
            res += dist[start][end]

        return res

        
def main():
    sol = Solution()
    print(sol.minimumCost(source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]))
    print(sol.minimumCost(source = "aaaa", target = "bbbb", original = ["a","c"], changed = ["c","b"], cost = [1,2]))
    print(sol.minimumCost(source = "abcd", target = "abce", original = ["a"], changed = ["e"], cost = [10000]))

if __name__ == '__main__':
    main()