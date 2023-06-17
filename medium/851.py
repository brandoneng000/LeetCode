from typing import List
import collections

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        wealth = collections.defaultdict(list)

        for a, b in richer:
            wealth[b].append(a)

        res = [None] * len(quiet)

        def dfs(node):
            if res[node] is None:
                res[node] = node
                for child in wealth[node]:
                    c = dfs(child)
                    if quiet[c] < quiet[res[node]]:
                        res[node] = c
            return res[node]

        return list(map(dfs, range(len(quiet))))

def main():
    sol = Solution()
    print(sol.loudAndRich(richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0]))
    print(sol.loudAndRich(richer = [], quiet = [0]))

if __name__ == '__main__':
    main()