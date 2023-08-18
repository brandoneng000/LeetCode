from typing import List

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = { i:[] for i in range(n) }
        res = 0

        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)
        
        for a in graph:
            for b in graph:
                if a == b:
                    continue

                count = len(graph[a]) + len(graph[b]) - (a in graph[b])
                res = max(res, count)
            
        return res

def main():
    sol = Solution()
    print(sol.maximalNetworkRank(n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]))
    print(sol.maximalNetworkRank(n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]))
    print(sol.maximalNetworkRank(n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]))

if __name__ == '__main__':
    main()