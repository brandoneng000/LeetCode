from typing import List
from collections import defaultdict

class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        def dfs(index: int, prev: int, dist: int, signal_speed: int, graph: dict):
            count = dist > 0 and (dist % signal_speed) == 0
            pairs = 0

            for j, weight in graph[index]:
                if j != prev:
                    cur_count = dfs(j, index, dist + weight, signal_speed, graph)
                    pairs += count * cur_count
                    count += cur_count
            
            return pairs if index == prev else count

        n = len(edges) + 1
        graph = defaultdict(list)
        res = [0] * n
        
        for a, b, weight in edges:
            graph[a].append([b, weight])
            graph[b].append([a, weight])

        for i in range(n):
            res[i] = dfs(i, i, 0, signalSpeed, graph)

        return res


def main():
    sol = Solution()
    print(sol.countPairsOfConnectableServers(edges = [[0,1,1],[1,2,5],[2,3,13],[3,4,9],[4,5,2]], signalSpeed = 1))
    print(sol.countPairsOfConnectableServers(edges = [[0,6,3],[6,5,3],[0,3,1],[3,2,7],[3,1,6],[3,4,2]], signalSpeed = 3))

if __name__ == '__main__':
    main()